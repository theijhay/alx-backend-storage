#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
import redis
from functools import wraps

store = redis.Redis()
# Connect to Redis server


def count_url_access(method):
    """ counts time for url access """
    @wraps(method)
    def wrapper(url):
        # Check if URL data is cached
        keys = "cached:" + url
        datas = store.get(cached_key)
        if datas:
            return datas.decode("utf-8")
        # Return cached data

        # If not cached, track access count and cache the result
        counter = "count:" + url
        fetch = method(url)  # Call the original function to fetch HTML content

        store.incr(count_key)  # Increment access count for this URL
        store.set(cached_key, html)  # Cache the HTML content
        store.expire(cached_key, 10)
        # Set expiration time for the cache (10 seconds)
        return fetch
    return wrapper


@count_url_access  # Apply the decorator to the get_page function
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)  # Fetch HTML content from the URL
    return res.text  # Return the HTML content as a string
