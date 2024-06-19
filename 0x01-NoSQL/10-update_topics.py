#!/usr/bin/env python3
"""
Rename Schooll Topics
"""


def update_topics(mongo_collection, name, topics):

    """
    changes all topics of schools
    document based on the name

    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
