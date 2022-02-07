class DLL():
    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.key) + ':' + str(self.val)


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()
        self.start = None
        self.end = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(key)
            self.append(node)
            return node.val
        else:
            return -1

    def delete(self, key):
        if key not in self.cache:
            return
        node = self.cache[key]
        del self.cache[node.key]

        if node == self.start and node == self.end:
            self.start = None
            self.end = None

        elif node == self.start:
            self.start = node.next
            self.start.prev = None

        elif node == self.end:
            self.end = self.end.prev
            self.end.next = None
        else:
            l = node.prev
            r = node.next
            l.next, r.prev = r, l

    def append(self, node):
        if not self.cache:
            self.start = node
        else:
            self.end.next, node.prev = node, self.end

        self.end = node
        self.cache[node.key] = node

    def put(self, key: int, value: int) -> None:
        node = DLL(key, value)

        self.delete(key)

        if len(self.cache) == self.cap:
            self.delete(self.start.key)
        self.append(node)


# Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache(2)
print("put 1", lRUCache.put(1, 1))
print("put 2", lRUCache.put(2, 2))
print("get 1", lRUCache.get(1))
print("put 3", lRUCache.put(3, 3))
print("get 2", lRUCache.get(2))
print("put 4", lRUCache.put(4, 4))
print("get 1", lRUCache.get(1))
print("get 3", lRUCache.get(3))
print("get 4", lRUCache.get(4))
