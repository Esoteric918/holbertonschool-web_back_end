#!/usr/bin/env python3
''' init func to list all documents in a collection '''

from pymongo import MongoClient

def list_all(mongo_collection):
    ''' list all documents in a collection '''
    return mongo_collection.find()
