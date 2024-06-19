#!/usr/bin/env python3

"""
Module: log_stats

This module connects to a MongoDB database
and retrieves statistics from the
logs collection of an Nginx server. It counts
and prints the total number of
logs and the number of logs for each HTTP method
(GET, POST, PUT, PATCH, DELETE).
Additionally, it counts and prints the number of
status check logs (GET requests to /status).
"""

from pymongo import MongoClient

def log_stats():
    """
    Retrieve and print log statistics from the
    logs collection in MongoDB.

    This function connects to the MongoDB server
    running on localhost, accesses
    the logs.nginx collection, and counts the total
    number of log entries as
    well as the number of log entries for each HTTP
    method. It also counts the
    number of status check logs (GET requests to
    /status) and prints all these
    statistics.
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
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")

if __name__ == "__main__":
    log_stats()
