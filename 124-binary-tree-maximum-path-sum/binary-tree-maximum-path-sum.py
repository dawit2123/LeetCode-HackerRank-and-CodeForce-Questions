# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def dfs(root):
            if not root:
                return 0
            left_max= dfs(root.left)
            right_max= dfs(root.right)
            left_max= max(left_max, 0)
            right_max= max(right_max, 0)
            res[0] = max(res[0], left_max + root.val + right_max)
            return max(left_max+root.val, root.val+right_max)
        dfs(root)
        return res[0]