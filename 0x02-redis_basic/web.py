#!/usr/bin/env python3
"""
Redis client module
"""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to a method"""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Increment call count and invoke method"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    """Decorator to track method call history"""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Store method inputs and outputs"""
        in_key = f"{method.__qualname__}:inputs"
        out_key = f"{method.__qualname__}:outputs"
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


def replay(fn: Callable) -> None:
    """Display call history of a method"""
    if fn is None or not hasattr(fn, "__self__"):
        return
    redis_store = getattr(fn.__self__, "_redis", None)
    if not isinstance(redis_store, redis.Redis):
        return
    fxn_name = fn.__qualname__
    in_key = f"{fxn_name}:inputs"
    out_key = f"{fxn_name}:outputs"
    fxn_call_count = int(redis_store.get(fxn_name, 0))
    print(f"{fxn_name} was called {fxn_call_count} times:")
    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print(f"{fxn_name}(*{fxn_input.decode('utf-8')}) -> {fxn_output}")


class Cache:
    """Cache class for Redis storage"""
    def __init__(self) -> None:
        """Initialize cache"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return key"""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """Retrieve data from Redis"""
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """Get string from Redis"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Get integer from Redis"""
        return self.get(key, lambda x: int(x))
