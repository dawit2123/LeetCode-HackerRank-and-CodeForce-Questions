# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        res=[]
        if not root:
            return []
        queue.append(root)
        while len(queue)>0:
            cur=[]
            for i in range(len(queue)):
                node=queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur)
        for i in range(len(res)):
            if i%2==0:
                continue
            else:
                res[i]= res[i][::-1]
        return res