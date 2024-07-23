#!/usr/bin/env python3
"""Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs

    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """
    def __init__(self):
        """Initialize the class with the parent's init method"""
        super().__init__()

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to a given key, or None"""
        if key is None:
            return None
        return self.cache_data.get(key)
