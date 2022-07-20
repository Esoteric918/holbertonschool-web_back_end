#!/usr/bin/env python3
'''pymongo insert_school.py'''

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    '''insert_school'''
    return mongo_collection.insert_one(kwargs).inserted_id
