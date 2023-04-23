#!/usr/bin/env python3
"""Task 0's module.
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """A Cache class.
    """
    def __init__(self):
        """Initializes the class.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis using a random key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Gets data from Redis.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """Gets data from Redis as a string.
        """
        return self.get(key, str)
    
    def get_int(self, key: str) -> int:
        """Gets data from Redis as an integer.
        """
        return self.get(key, int)
