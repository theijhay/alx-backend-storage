#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """Provide statistics about Nginx logs stored in MongoDB."""
    stats = {}

    # If option is provided, count documents with specific method
    if option:
        count = mongo_collection.count_documents({"method": {"$regex": option}})
        print(f"\tmethod {option}: {count}")
        return

    # Count total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Display methods and their counts
    print("Methods:")
    for method in METHODS:
        log_stats(mongo_collection, method)

    # Count number of logs with path="/status"
    status_check_count = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    # Connect to MongoDB and select nginx collection
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    # Call log_stats function
    log_stats(nginx_collection)
