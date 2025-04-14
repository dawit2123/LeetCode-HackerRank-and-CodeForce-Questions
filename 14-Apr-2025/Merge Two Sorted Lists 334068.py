# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        head=dummy
        while list1 and list2:
            if list1.val<list2.val:
                dummy.next=list1
                dummy=dummy.next
                list1=list1.next
            else:
                dummy.next=list2
                dummy=dummy.next
                list2=list2.next
        if list1:
            dummy.next=list1
        if list2:
            dummy.next=list2
        return head.next
        