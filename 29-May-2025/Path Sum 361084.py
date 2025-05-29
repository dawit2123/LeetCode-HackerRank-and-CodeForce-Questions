# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cur_sum):
            if not root:
                return
            cur_sum+=root.val
            if cur_sum==targetSum and not root.left and not root.right:
                return True
            return dfs(root.left, cur_sum) or dfs(root.right, cur_sum)
        return True if dfs(root, 0)==True else False