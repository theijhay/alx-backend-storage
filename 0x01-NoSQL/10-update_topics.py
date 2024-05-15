#!/usr/bin/env python3
"""change all topics of a school document based on the name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update topics of a school document in the collection.

    Args:
        mongo_collection: pymongo collection object.
        name: Name of the school to update.
        topics: List of new topics.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation.
    """
    # Update documents matching the specified name
    update_result = mongo_collection.update_many(
        {"name": name},  # Specify the document to update based on name
        {"$set": {"topics": topics}}  # Set the new topics
    )

    return update_result
