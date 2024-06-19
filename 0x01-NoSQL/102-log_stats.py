#!/usr/bin/env python3

"""
Module to display log statistics
"""

from pymongo import MongoClient

def log_stats():

    """
    Display statistics for logs.

    Connects to MongoDB on localhost and
    retrieves various statistics
    from the logs.nginx collection, including
    total logs, counts for
    each HTTP method (GET, POST, PUT, PATCH, DELETE),
    and status check
    logs (GET requests to /status).
    """

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    total = logs_collection.count_documents({})
    get = logs_collection.count_documents({"method": "GET"})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    delete = logs_collection.count_documents({"method": "DELETE"})
    path = logs_collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total} logs")
    print("Methods:")
    print(f"\tGET: {get}")
    print(f"\tPOST: {post}")
    print(f"\tPUT: {put}")
    print(f"\tPATCH: {patch}")
    print(f"\tDELETE: {delete}")
    print(f"{path} status checks")

if __name__ == "__main__":
    log_stats()
