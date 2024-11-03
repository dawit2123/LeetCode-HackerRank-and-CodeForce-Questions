# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(root, val_list):
            if not root:
                return
            val_list.append(root.val)
            print(val_list)
            if sum(val_list)==targetSum and not root.left and not root.right:
                res.append(val_list)
                return
            dfs(root.left, val_list.copy())
            dfs(root.right, val_list.copy())
        dfs(root, [])
        return res