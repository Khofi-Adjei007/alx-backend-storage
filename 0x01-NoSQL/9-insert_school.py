#!/usr/bin/env python3


"""
 We are going to Insert docs in Python
"""
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):

    """
     inserts new document in
      collection on kwargs

    :param mongo_collection:
    :param kwargs:
    :return:
    """
    new_results = mongo_collection.insert_one(kwargs)
    return new_results.inserted_id
