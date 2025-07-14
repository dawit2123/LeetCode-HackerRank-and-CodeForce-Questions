# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary_values=[]
        cur=head
        while cur:
            binary_values.append(str(cur.val))
            cur=cur.next
        return int(''.join(binary_values), 2)