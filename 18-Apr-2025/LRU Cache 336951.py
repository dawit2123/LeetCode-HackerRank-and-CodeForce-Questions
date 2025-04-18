# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key=0, val=0):
        self.key=key
        self.val=val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hash_map={}
        self.left, self.right=Node(), Node()
        self.left.next, self.right.prev= self.right, self.left

    def insert(self, node):
        prev, nxt= self.right.prev, self.right
        prev.next=nxt.prev=node
        node.prev, node.next= prev, nxt

    def remove(self, node):
        prev, nxt= node.prev, node.next
        prev.next, nxt.prev= nxt, prev

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            self.insert(self.hash_map[key])
            return self.hash_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
        node=Node(key, value)
        self.insert(node)
        self.hash_map[key]=node
        if len(self.hash_map)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.hash_map[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)