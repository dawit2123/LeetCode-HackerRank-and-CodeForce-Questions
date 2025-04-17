# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values=[]
        cur=head
        while cur:
            values.append(cur.val)
            cur=cur.next
        left, right= 0, len(values)-1
        while left<=right:
            if values[left]!=values[right]:
                return False
            left+=1
            right-=1
        return True
        
