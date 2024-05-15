#!/usr/bin/env python3
"""The list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Find schools covering the specified topic"""
    return mongo_collection.find({"topics": {"$in": [topic]}})
