# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        carry=0
        while l1 or l2 or carry:
            l1_val= l1.val if l1 else 0
            l2_val= l2.val if l2 else 0
            temp= l1_val+l2_val+carry
            result=temp%10
            carry=temp//10
            cur.next=ListNode(result)
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            cur=cur.next
        # if l1:
        #     cur.next=l1
        # if l2:
        #     cur.next=l2
        return dummy.next
            