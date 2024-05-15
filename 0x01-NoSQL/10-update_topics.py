#!/usr/bin/env python3
"""change all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Use update_many() method to update
    documents with the specified name
    """
    result = mongo_collection.update_many(
        {"name": name},  # Filter documents by name
        {"$set": {"topics": topics}}  # the new list of topics
    )
    """Print the number of documents modified"""
    print("Number of documents updated:", result.modified_count)
