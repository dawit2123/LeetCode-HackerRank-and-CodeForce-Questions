class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.head=None

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
            return
        node=Node(val, self.head)
        self.head=node

    def get(self, index: int) -> int:
        i=0 
        cur=self.head
        while cur:
            print(cur.val)
            if i==index:
                return cur.val
            else:
                i+=1
                cur=cur.next
        return -1

    def addAtTail(self, val: int) -> None:
        cur=self.head
        if not self.head:
            self.head=Node(val)
            return
        while cur.next:
            cur=cur.next
        node=Node(val)
        cur.next=node
        
    def addAtIndex(self, index: int, val: int) -> None:
       i=0
       cur=self.head
       if index==0:
        self.head=Node(val)
        self.head.next=cur
       while cur:
        i+=1
        if i==index:
            node=Node(val)
            node.next=cur.next
            cur.next=node
            return
        cur=cur.next

    def deleteAtIndex(self, index: int) -> None:
        i=0
        cur=self.head
        previous_node=None
        while cur and i!=index:
            previous_node=cur
            cur=cur.next
            i+=1
        if not cur:
            return 
        if index==0:
            self.head=self.head.next
            return
        previous_node.next=previous_node.next.next
        cur=None
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)