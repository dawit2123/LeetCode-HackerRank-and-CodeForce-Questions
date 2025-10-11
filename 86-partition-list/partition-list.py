# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_node, right_node= ListNode(), ListNode()
        left_tail, right_tail= left_node, right_node
        cur=head
        while cur:
            if cur.val<x:
                left_tail.next=ListNode(cur.val)
                left_tail=left_tail.next
            else:
                right_tail.next=ListNode(cur.val)
                right_tail=right_tail.next
            cur=cur.next
        left_tail.next=right_node.next
        return left_node.next