class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


# Time  O(1) for get() and put()
# Space  O(capacity)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.first = ListNode(-1, -1)
        self.last = ListNode(-1, -1)
        self.first.next = self.last
        self.last.prev = self.first

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        
        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)
        
        if len(self.dic) > self.capacity:
            node = self.first.next
            self.remove(node)
            del self.dic[node.key]

    def add(self, node):
        prev = self.last.prev
        prev.next = node
        self.last.prev = node
        node.prev = prev
        node.next = self.last
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# OrderedDict

# Time  O(1) for get() and put()
# Space  O(capacity)
import collections

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        self.dic.move_to_end(key)
        return self.dic[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)