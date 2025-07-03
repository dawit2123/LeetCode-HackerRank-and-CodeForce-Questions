# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Edge Case: if k=0 then the target will be returned immediately
        if not k:
            return [target.val]

        # Creating a queue and a graph
        queue= deque([root])
        graph= defaultdict(list)
        while queue:   
            node= queue.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
        result=[]
        # Start traversing from the target to it's neighbours
        visited=set([target])
        queue=deque([(target, 0)])
        while queue:
            node, length= queue.popleft()
            if length==k:
                result.append(node.val)
            else:
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append((neighbour, length+1))
        return result