#!/usr/bin/env python3
"""LRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines a LRU caching system"""
    def __init__(self):
        """Initialize the class with the parent's init method"""
        super().__init__()
        self.used = []

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is None or item is None:
            return
        else:
            length = len(self.cache_data) 
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.used[0]}")
                del self.cache_data[self.used[0]]
                del self.used[0]
            if key in self.used:
                del self.used[self.used.index(key)]
            self.used.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to a given key, or None"""
        if key is not None and key in self.cache_data.keys():
            del self.used[self.used.index(key)]
            self.used.append(key)
            return self.cache_data[key]
        return None
