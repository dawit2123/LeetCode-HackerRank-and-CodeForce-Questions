# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur_sum=0
        def dfs(node):
            if not node:
                return
            nonlocal cur_sum
            dfs(node.right)
            temp= node.val
            node.val+=cur_sum
            cur_sum+=temp
            dfs(node.left)
        dfs(root)
        return root
            