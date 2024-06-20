#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """Decorator to cache and count get_page calls"""
    @wraps(fn)
    def wrapper(url: str) -> str:
        """Check cache and track call count"""
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(url)
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(url, response, ex=10)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """Make a HTTP request to a URL"""
    response = requests.get(url)
    return response.text
