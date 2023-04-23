#!/usr/bin/env python3
"""Task 0's module.
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of the Cache class are called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Counts how many times methods of the Cache class are called.
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular function.
    """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Stores the history of inputs and outputs for a particular function.
        """
        self._redis.rpush(inputs, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs, output)
        return output
    return wrapper


def replay(method: Callable):
    """Displays the history of calls of a particular function.
    """
    redis_client = redis.Redis()
    method_name = method.__qualname__
    inputs = redis_client.lrange(method_name + ":inputs", 0, -1)
    outputs = redis_client.lrange(method_name + ":outputs", 0, -1)
    count = redis_client.get(method_name).decode("utf-8")
    print("{} was called {} times:".format(method_name, count))
    for i, j in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name, i.decode("utf-8"), j.decode("utf-8")))


class Cache:
    """A Cache class.
    """
    def __init__(self):
        """Initializes the class.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
