# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous, current = dummy, head

        while current and current.next:
            npn = current.next.next
            second = current.next

            second.next = current
            current.next = npn
            previous.next = second

            previous = current
            current = npn
        
        return dummy.next