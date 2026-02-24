class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, current_value: int) -> int:
            if node is None:
                return 0
            current_value = (current_value << 1) | node.val
            if node.left is None and node.right is None:
                return current_value
            left_sum = dfs(node.left, current_value)
            right_sum = dfs(node.right, current_value)
            return left_sum + right_sum
        return dfs(root, 0)