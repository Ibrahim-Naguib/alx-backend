#!/usr/bin/env python3
"""FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a FIFO caching system"""
    def __init__(self):
        """Initialize the class with the parent's init method"""
        super().__init__()

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            k = list(self.cache_data.keys())[0]
            print(f"DISCARD: {k}")
            self.cache_data.pop(k)
        self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to a given key, or None"""
        if key is None:
            return None
        return self.cache_data.get(key)
