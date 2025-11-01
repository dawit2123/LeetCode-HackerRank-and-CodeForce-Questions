# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set=set(nums)
        node=ListNode()
        node.next=head
        cur=node
        while cur and cur.next:
            while cur and cur.next and cur.next.val in nums_set:
                cur.next=cur.next.next
            cur=cur.next
        return node.next
        