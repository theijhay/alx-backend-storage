#!/usr/bin/env python3
"""Python function that inserts a new document in a
collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """insert a new document into the collection"""
    result = mongo_collection.insert_one(kwargs)
    """Return the inserted document's _id"""
    return result.inserted_id
