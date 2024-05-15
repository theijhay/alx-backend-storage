#!/usr/bin/env python3
"""Provide statistics about Nginx logs stored in MongoDB"""

from pymongo import MongoClient
from collections import Counter


if __name__ == "__main__":
    # Connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    # Get the total number of logs
    total_logs = logs.count_documents({})
    print(f"{total_logs} logs")

    # Print the method types and counts
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Get the number of logs with method=GET and path=/status
    status_logs = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_logs} status check")

    # Get the top 10 most present IPs
    print("IPs:")
    ip_counts = logs.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip_count in ip_counts:
        ip = ip_count["_id"]
        count = ip_count["count"]
        print(f"\t{ip}: {count}")
