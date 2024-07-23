#!/usr/bin/env python3
"""LFU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines a LFU caching system"""
    def __init__(self):
        """Initialize the class with the parent's init method"""
        super().__init__()
        self.order = []
        self.freq = {}

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order.remove(key)
            self.order.append(key)
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                lfu_keys = [k for k in self.order if self.freq[k] == min_freq]
                lfu_key = lfu_keys[0]

                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                self.order.remove(lfu_key)

            self.cache_data[key] = item
            self.freq[key] = 1
            self.order.append(key)

    def get(self, key):
        """Return the value linked to a given key, or None"""
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
