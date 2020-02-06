class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.front = self.back = None
        self.cache = dict()
        self.cap = capacity
        self.size = 0

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self._remove(node)
            self._push(node)
            return node.key
        else:
            return - 1

    def put(self, key: int, value: int) -> None:
        found_node = self.cache.get(key)
        if found_node:
            self._remove(self.cache[key])
        elif self.size == self.cap:
            self._remove(self.front)

        node = Node(key, value)
        self._push(node)

    def _push(self, node):
        if self.size == 0:
            self.back = node
            self.front = node
        else:
            self.back.next = node
            node.prev = self.back
            self.back = node

        self.cache[node.key] = node
        self.size += 1

    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.back:
            self.back = self.back.prev

        if node == self.front:
            self.front = self.front.next

        del self.cache[node.key]
        self.size -= 1


commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
lru_cache = None

for com, arg in zip(commands, arguments):
    if com == "LRUCache":
        lru_cache = LRUCache(*arg)
    elif com == "put":
        lru_cache.put(*arg)

    elif com == "get":
        lru_cache.get(*arg)
