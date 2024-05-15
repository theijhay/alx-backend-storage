#!/usr/bin/env python3
""" A store method that takes a data argument and returns a string."""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts times the cache method is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """returns the wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        # Initializes redis
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Creates a random
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        # Returns a key
        return key

    def get(self, key: str, fn: Callable = None):
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def decode_utf8(self, value: bytes) -> str:
        return value.decode('utf-8')

    def get_str(self, key: str) -> str:
        return self.get(key, self.decode_utf8)

    def get_int(self, key: str) -> int:
        return self.get(key, int)

    '''def count_calls(method: Callable) -> Callable:
    """Counts times the cache method is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """returns the wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper'''


def call_history(method: Callable) -> Callable:

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # Append input arguments to the inputs list
        self._redis.rpush(inputs_key, str(args))

        # Execute the wrapped function to retrieve the output
        output = method(self, *args, **kwargs)

        # Store the output in the outputs list
        self._redis.rpush(outputs_key, str(output))

        return output
    return wrapper


# Decorate Cache.store with call_history
Cache.store = call_history(Cache.store)
