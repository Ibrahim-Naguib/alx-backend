#!/usr/bin/env python3
"""LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a LIFO caching system"""
    def __init__(self):
        """Initialize the class with the parent's init method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                k = self.order.pop()
                print(f"DISCARD: {k}")
                self.cache_data.pop(k)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Return the value linked to a given key, or None"""
        if key is None:
            return None
        return self.cache_data.get(key)
