# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # first step is to get the middle
        slow, fast= head, head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        previous= None
        current= slow
        while current:
            temp=current.next
            current.next=previous
            previous, current= current, temp
        # Go over starting from the head and previous to till they're null
        while previous:
            if previous.val!=head.val:
                return False
            previous, head= previous.next, head.next
        return True