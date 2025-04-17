# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverting the pointers until the middle
        slow, fast= head, head
        prev=None
        res=0
        while fast and fast.next:
            temp=slow.next
            fast=fast.next.next
            slow.next=prev
            prev=slow
            slow=temp
        while slow:
            res=max(res, prev.val + slow.val)
            slow=slow.next
            prev=prev.next
        return res