#!/usr/bin/env python3
"""
Module to get top students
"""

def top_students(mongo_collection):
    """
    Get all students sorted by average score.
    
    :param mongo_collection: pymongo collection object
    :return: Cursor with students sorted by average score
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": 1,
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
