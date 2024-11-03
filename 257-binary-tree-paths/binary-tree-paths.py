# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        if not root.left and not root.right:
            res.append(str(root.val))
            return res
        def dfs(root, path):
            if not root:
                return
            path+=f"->{root.val}"
            if not root.left and not root.right:
                res.append(path)
                return
            dfs(root.left, path)
            dfs(root.right, path)
        dfs(root.left, f"{root.val}")
        dfs(root.right, f"{root.val}")
        return res