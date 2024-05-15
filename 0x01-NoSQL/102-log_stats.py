#!/usr/bin/env python3
"""Provide statistics about Nginx logs stored in MongoDB"""

from pymongo import MongoClient
from collections import Counter

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Provide statistics about Nginx logs stored in MongoDB.
    Args:
        mongo_collection: pymongo collection object for the nginx logs.
        option: Optional parameter to specify a particular method.
    Returns:
        None
    """
    stats = {}

    # If option is provided, count documents with specific method
    if option:
        count = mongo_collection.count_documents(
                {"method": {"$regex": option}})
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

    # Find the top 10 most common IP addresses
    ip_counter = Counter(log["ip"] for log in mongo_collection.find())
    print("IPs:")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip}: {count}")


if __name__ == "__main__":
    # Connect to MongoDB and select nginx collection
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    # Call log_stats function
    log_stats(nginx_collection)
