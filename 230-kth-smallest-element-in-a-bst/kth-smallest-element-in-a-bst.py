# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_arr=[]
        def inorder_traversal(root):
            if not root:
                return
            inorder_traversal(root.left)
            sorted_arr.append(root.val)
            inorder_traversal(root.right)
            return
        inorder_traversal(root)
        return sorted_arr[k-1]