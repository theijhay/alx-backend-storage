#!/usr/bin/env python3
"""A store method that takes a data argument and returns a string. """

import uuid
import redis


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
        """store method that takes a data"""

    def store(self, data: str | bytes | int | float) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
