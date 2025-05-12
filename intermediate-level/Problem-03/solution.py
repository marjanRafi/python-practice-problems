# Implement an LRU Cache (Least Recently Used)

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    print(f"Get 2: {lru_cache.get(2)}") # returns 2
    lru_cache.put(4, 4) # evicts key 1
    print(f"Get 1: {lru_cache.get(1)}") # returns -1 (not found)