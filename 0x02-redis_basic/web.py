#!/usr/bin/env python3
"""Task 5's module.
"""
import redis
import requests
from typing import Callable
from functools import wraps


redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """Caches data from a particular URL.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """Caches data from a particular URL.
        """
        if redis_store.get(url):
            return redis_store.get(url).decode("utf-8")
        else:
            data = method(url)
            redis_store.setex(url, 10, data)
            return data
    return wrapper


@data_cacher
def get_page(url: str) -> str:
    """Gets the HTML content of a particular URL.
    """
    return requests.get(url).text
