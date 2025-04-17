# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        dummy=head
        cur=dummy
        nxt=cur.next
        while nxt:
            if nxt.val!=cur.val:
                cur.next=nxt
                cur=cur.next
            nxt=nxt.next
            cur.next=None
        return dummy
