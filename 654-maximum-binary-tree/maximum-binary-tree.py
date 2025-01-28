# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(sub_nums):
            if not sub_nums:
                return None
            #getting the max
            max_num= max(sub_nums)
            root= TreeNode(max_num)
            index= sub_nums.index(max_num)
            root.left= dfs(sub_nums[:index])
            root.right= dfs(sub_nums[index+1:])
            return root
        return dfs(nums)