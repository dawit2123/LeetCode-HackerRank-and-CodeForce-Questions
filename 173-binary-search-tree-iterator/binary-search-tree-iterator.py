# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr=root
        self.stack=[]
        while self.curr:
            self.stack.append(self.curr)
            self.curr=self.curr.left
    def next(self) -> int:
                res=self.stack.pop()
                print(res)
                self.curr=res.right
                while self.curr:
                    self.stack.append(self.curr)
                    self.curr=self.curr.left
                return res.val
    def hasNext(self) -> bool:
        return True if len(self.stack)>0 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()