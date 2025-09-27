# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.val = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        ans = 0
        q = deque([node])
        while q:
            node = q.popleft()
            ans += node.val
            for child in node.children.values():
                q.append(child)
        return ans