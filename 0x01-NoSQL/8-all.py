#!/usr/bin/env python3

"""
listing all available docs in python
"""


def list_all(mongo_collection):

    """
    lists all available docs in a collection

    :param mongo_collection:
    :return:
    """
    return mongo_collection.find()
