# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        if not root:
            return False
        
        queue = deque()
        queue.append(root)
        level = -1
        
        while queue:
            level += 1
            size = len(queue)
            prev = 0
            
            for i in range(size):
                curr = queue.popleft()

                if level == 0 and curr.val % 2 == 0:
                    return False

                if i == 0:
                    if (level % 2 == 0 and curr.val % 2 == 1) or (level % 2 == 1 and curr.val % 2 == 0):
                        prev = curr.val
                    else:
                        return False
                else:
                    if level % 2 == 1:
                        if curr.val % 2 == 0 and prev > curr.val:
                            prev = curr.val
                        else:
                            return False
                    else:
                        if curr.val % 2 == 1 and prev < curr.val:
                            prev = curr.val
                        else:
                            return False

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)

        return True