class ArrayMap:
    def __init__(self):
        self.items = []

    def put(self, key, val=None):
        for i, (k, v) in enumerate(self.items):
            if k == key:
                self.items[i] = (key, val)
                return
            elif k > key:
                self.items.insert(i, (key, val))
                return
        self.items.append((key, val))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v
        return None

    def delete(self, key):
        for i, (k, v) in enumerate(self.items):
            if k == key:
                self.items.pop(i)
                return
        return

    def length(self):
        return len(self.items)

    def contains(self, key):
        for k, v in self.items:
            if k == key:
                return True
        return False
