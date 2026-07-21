class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}         # Maps key -> node for O(1) access
        self.capacity = capacity

        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])  # Remove from current position
            self.insert(self.cache[key])  # Re-insert at new (most recent) position
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])   # Remove old node if updating
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])     # Add to most recent

        # If adding a pair exceeds capacity
        if len(self.cache) > self.capacity:
            lru = self.head.next  # First real node after dummy head
            self.remove(lru)     # Remove from linked list
            del self.cache[lru.key]   # Remove from hashmap
