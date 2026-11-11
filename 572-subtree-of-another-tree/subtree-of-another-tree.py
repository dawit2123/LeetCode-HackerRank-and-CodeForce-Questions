class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        def selfTree(s, t):
            if not s and not t:
                return True
            if not s or not t or s.val!=t.val:
                return False
            return selfTree(s.left, t.left) and selfTree(s.right, t.right)
        if selfTree(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))