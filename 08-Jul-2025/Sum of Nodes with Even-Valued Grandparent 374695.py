# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root,dad,grand_parent):
            if not root:
                return 0
            x=0
            if(grand_parent%2==0):
                x=root.val
            x+=dfs(root.left,root.val,dad)
            x+=dfs(root.right,root.val,dad)
            return x

        return dfs(root,1,1)