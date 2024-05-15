#!/usr/bin/env python3
"""
Web cache module
"""
import functools
import requests
import redis


def cache_with_expiration(method):
    """
    Cache the result of a method with expiration
    """
    @functools.wraps(method)
    def wrapper(self, url):
        key = f"content:{url}"
        content = self._redis.get(key)
        if content is None:
            content = method(self, url)
            self._redis.set(key, content, ex=10)
            self._redis.incr(f"count:{url}")
        return content
    return wrapper


class WebCache:
    """
    Web cache class
    """
    def __init__(self):
        self._redis = redis.Redis()

    @cache_with_expiration
    def get_page(self, url: str) -> str:
        """
        Get the HTML content of a particular URL and cache it
        """
        response = requests.get(url)
        content = response.content
        return content
