class LinkedList:
    def __init__(self, value, prev, nxt):
        self.val, self.prev, self.next= value, prev, nxt
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity=k
        self.left=LinkedList(0, None, None)
        self.right=LinkedList(0, self.left, None)
        self.left.next=self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        item=LinkedList(value, self.right.prev, self.right)
        self.right.prev.next=item
        self.right.prev=item
        self.capacity-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next= self.left.next.next
        self.left.next.prev=self.left
        self.capacity+=1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        front_value=self.left.next.val
        return front_value

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        rear_value= self.right.prev.val
        return rear_value

    def isEmpty(self) -> bool:
        return self.left.next==self.right

    def isFull(self) -> bool:
        return self.capacity==0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()