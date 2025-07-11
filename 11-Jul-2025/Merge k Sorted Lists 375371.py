# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists and len(lists)==0:
            return None
        while len(lists)>1:
            merged_lists=[]
            for i in range(0, len(lists), 2):
                left= lists[i]
                right=lists[i+1] if i+1<len(lists) else None
                merged_lists.append(self.merge(left,right))
            lists=merged_lists
        return lists[0]
    def merge(self, left, right):
        dummy=ListNode()
        cur=dummy
        while left and right:
            if left.val<right.val:
                cur.next=left
                left=left.next
            else:
                cur.next=right
                right=right.next
            cur=cur.next
        if left:
            cur.next=left
        if right:
            cur.next=right
        return dummy.next