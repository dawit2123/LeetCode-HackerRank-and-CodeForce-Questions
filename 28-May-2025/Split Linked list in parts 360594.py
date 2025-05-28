# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next        
        part_size = length // k
        larger_parts = length % k
        result = []
        current = head
        for i in range(k):
            sublist_size = part_size + 1 if i < larger_parts else part_size
            if sublist_size == 0:
                result.append(None)
            else:
                sublist_head = current
                for _ in range(sublist_size - 1):
                    current = current.next
                next_node = current.next
                current.next = None
                result.append(sublist_head)
                current = next_node
        return result