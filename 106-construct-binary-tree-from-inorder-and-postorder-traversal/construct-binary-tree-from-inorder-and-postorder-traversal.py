# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        root=TreeNode(postorder[-1])
        pivot=inorder.index(postorder[-1])
        root.left=self.buildTree(inorder[:pivot], postorder[:pivot])
        root.right=self.buildTree(inorder[pivot+1:], postorder[pivot:-1])
        return root