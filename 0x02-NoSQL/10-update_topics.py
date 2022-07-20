#!/usr/bin/env python3
'''Python function to change the topics of a school'''

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    '''Python function to change the topics of a school'''
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}}).modified_count
