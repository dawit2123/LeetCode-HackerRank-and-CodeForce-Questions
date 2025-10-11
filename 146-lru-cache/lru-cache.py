class Node:
    def __init__(self, key, value):
        self.key=key
        self.val=value
        self.prev, self.next= None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map={}
        self.capacity=capacity
        self.left, self.right= Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev= self.right, self.left

    def insert(self, node):
        prev, nxt= self.right.prev, self.right
        prev.next=node
        nxt.prev=node
        node.next=nxt
        node.prev=prev
    def remove(self, node):
        prev, nxt= node.prev, node.next
        prev.next= nxt
        nxt.prev=prev
    def get(self, key: int) -> int:
        if key in self.hash_map:
            node= self.hash_map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node= self.hash_map[key]
            self.remove(node)
            del self.hash_map[key]
        new_node= Node(key, value)
        self.insert(new_node)
        self.hash_map[key]=new_node
        if len(self.hash_map)>self.capacity:
            node= self.left.next
            self.remove(node)
            del self.hash_map[node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)