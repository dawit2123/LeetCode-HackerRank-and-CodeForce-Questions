# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(root, val_list, cur_sum):
            if not root:
                return
            val_list.append(root.val)
            cur_sum+=root.val
            if cur_sum==targetSum and not root.left and not root.right:
                res.append(val_list)
                return
            dfs(root.left, val_list.copy(), cur_sum)
            dfs(root.right, val_list.copy(), cur_sum)
        dfs(root, [], 0)
        return res