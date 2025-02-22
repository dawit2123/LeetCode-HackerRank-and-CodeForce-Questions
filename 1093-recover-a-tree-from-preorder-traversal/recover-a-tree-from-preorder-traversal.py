class Solution:
    def recoverFromPreorder(self, s: str) -> TreeNode:
        vp = []
        i = 0
        while i < len(s):
            depth = 0
            while i < len(s) and s[i] == '-':
                depth += 1
                i += 1
            num = 0
            while i < len(s) and s[i] != '-':
                num = num * 10 + int(s[i])
                i += 1
            vp.append((depth, num))
        stack = []
        root = None
        for depth, nodeVal in vp:
            node = TreeNode(nodeVal)
            while stack and stack[-1][0] >= depth:
                stack.pop()
            if stack:
                parent = stack[-1][1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            else:
                root = node
            stack.append((depth, node))
        return root