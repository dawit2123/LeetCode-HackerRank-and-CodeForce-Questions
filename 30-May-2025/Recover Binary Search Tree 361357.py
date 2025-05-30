# Problem: Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def recoverTree(self, root: Optional[TreeNode]) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		array = []
		def InOrder(node):
			if node != None:
				InOrder(node.left)
				array.append(node)
				InOrder(node.right)
		InOrder(root)
		length = len(array)
		first_node = array[0]
		second_node = array[-1]
		for i in range(1,length):
			if array[i].val < array[i-1].val:
				first_node = array[i-1]
				break
		for i in range(length-2,-1,-1):
			if array[i].val > array[i+1].val:
				second_node = array[i+1]
				break
		first_node.val , second_node.val = second_node.val , first_node.val