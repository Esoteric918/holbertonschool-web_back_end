#!/usr/bin/env python3
'''pymongo insert_school.py'''

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    ''' insert a school document '''
    if mongo_collection is None:
        return []
    return mongo_collection.insert_one(kwargs)
