#!/usr/bin/env python3
"""Task 0's module.
"""
import redis


class Cache:
    """A Cache class.
    """
    def __init__(self):
        """Initializes the class.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """Stores data in Redis using a random key.
        """
        key = self._redis.randomkey()
        self._redis.set(key, data)
        return key
