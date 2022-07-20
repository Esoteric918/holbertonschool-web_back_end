#!/usr/bin/env python3
''' init func to list all documents in a collection '''


def list_all(mongo_collection):
    """
    List all documents in a collection
    """
    for doc in mongo_collection.find():
        print(doc)
