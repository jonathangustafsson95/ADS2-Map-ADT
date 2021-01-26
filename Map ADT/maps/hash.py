class HashMap:
    def __init__(self, size):
        self.hash_func, self.size = my_hash, size
        self.items = [[] for _ in range(self.size)]

    def put(self, key, val='a value'):
        hash_val = self.hash_func(key, self.size)
        bucket = self.items[hash_val]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, val)
                return
        bucket.append((key, val))

    def get(self, key):
        hash_val = self.hash_func(key, self.size)
        bucket = self.items[hash_val]
        for i, (k, v) in enumerate(bucket):
            if key == k:
                return bucket[i]
        return False

    def delete(self, key):
        hash_val = self.hash_func(key, self.size)
        bucket = self.items[hash_val]
        for i, (k, v) in enumerate(bucket):
            if key == k:
                del bucket[i]
        return False

    def length(self):
        nr_keys = 0
        for cell in range(self.size):
            for _ in self.items[cell]:
                nr_keys += 1
        return nr_keys

    def contains(self, key):
        hash_key = self.hash_func(key, self.size)
        bucket = self.items[hash_key]
        for i, (k, v) in enumerate(bucket):
            if key == k:
                return True
        return False


def my_hash(key, size):
    return key % size
