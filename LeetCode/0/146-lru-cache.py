class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # indexing from latest (0) to oldest (capacity-1)
        self.keys = []
        self.values = []

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        key_idx = self.keys.index(key)
        value = self.values[key_idx]

        self.keys = [key] + self.keys[:key_idx] + self.keys[key_idx+1:]
        self.values = [value] + self.values[:key_idx] + self.values[key_idx+1:]

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            key_idx = self.keys.index(key)
            self.keys = [key] + self.keys[:key_idx] + self.keys[key_idx+1:]
            self.values = [value] + self.values[:key_idx] + self.values[key_idx+1:]
        elif len(self.keys) < self.capacity:
            self.keys.insert(0,key)
            self.values.insert(0,value)
        else:
            self.keys = [key] + self.keys[:-1]
            self.values = [value] + self.values[:-1]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)