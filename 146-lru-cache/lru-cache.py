class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hash_map={}
        self.left, self.right= Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev=self.right, self.left
    
    def add(self, node):
        prev, nxt= self.right.prev, self.right
        prev.next=nxt.prev=node
        node.prev, node.next= prev, nxt
    
    def remove(self, node):
        prev, nxt= node.prev, node.next
        prev.next, nxt.prev= nxt, prev

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node=self.hash_map[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            del self.hash_map[key]
        node=Node(key, value)
        self.hash_map[key]=node
        self.add(node)
        if len(self.hash_map)>self.capacity:
            node=self.left.next
            self.remove(node)
            del self.hash_map[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)