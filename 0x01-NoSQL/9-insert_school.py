#!/usr/bin/env python3
from pymongo import MongoClient

"""
Insert docs in Python
"""


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
