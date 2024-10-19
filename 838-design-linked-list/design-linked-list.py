class Node:
        def __init__(self, val=0, left=None, right=None):
            self.val=val
            self.left=left
            self.right=right
class MyLinkedList:

    def __init__(self):
        self.left_boundary, self.right_boundary=Node(), Node()
        self.left_boundary.right=self.right_boundary
        self.right_boundary.left=self.left_boundary

    def addAtHead(self, val: int) -> None:
        node, next, prev= Node(val), self.left_boundary.right, self.left_boundary
        node.right=next
        node.left=prev
        prev.right=node
        next.left=node

    def get(self, index: int) -> int:
        i=0
        cur=self.left_boundary.right
        while cur:
            if i==index and cur!=self.right_boundary:
                return cur.val
            else:
                i+=1
                cur=cur.right
        return -1
        
    def addAtTail(self, val: int) -> None:
        node, prev, next=Node(val), self.right_boundary.left, self.right_boundary
        node.right=next
        node.left=prev
        prev.right=node
        next.left=node

        
    def addAtIndex(self, index: int, val: int) -> None:
        i=0
        cur=self.left_boundary.right
        while cur:
            if i==index:
                node, prev, next= Node(val), cur.left, cur
                node.right=next
                node.left=prev
                prev.right=node
                next.left=node
                return
            else:
                cur=cur.right
                i+=1
            
       
    def deleteAtIndex(self, index: int) -> None:
        i=0
        cur=self.left_boundary.right
        while cur:
            if i==index and cur!=self.right_boundary:
                prev, next= cur.left, cur.right
                prev.right=next
                next.left=prev
                return
            else:
                i+=1
                cur=cur.right
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)