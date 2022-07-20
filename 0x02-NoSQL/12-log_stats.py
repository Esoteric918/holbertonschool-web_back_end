#!/usr/bin/env python3
''' script that provides some stats about Nginx logs stored in MongoDB'''

import pymongo

# Database: logs
# Collection: nginx
# Display (same as the example):
# first line: x logs where x is the number of documents in this collection
# second line: Methods:
# 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
# one line with the number of documents with:
# method=GET
# path=/status

def logStats():
    ''' function that provides some stats about Nginx logs stored in MongoDB'''
    client = pymongo.MongoClient()
    db = client["logs"]
    collection = db["nginx"]

    print(f"{collection.count_documents({})} 'logs' {collection.count_documents({})} 'nginx'")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print(f"{collection.count_documents({"method": "{method}"})}")
    print(f'{collection.count_documents({"method": "GET", "path": "/status"})}')

if__name__ == "__main__":
    logStats()
