#!/usr/bin/env python3
"""function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """ scholars placed by score """
    list = [
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ]
    return mongo_collection.aggregate(list)
