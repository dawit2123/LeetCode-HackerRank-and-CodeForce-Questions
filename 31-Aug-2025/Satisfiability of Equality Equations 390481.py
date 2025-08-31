# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = list(range(26))

        for equation in equations:
            var1_index = ord(equation[0]) - ord('a')
            var2_index = ord(equation[-1]) - ord('a')
            if equation[1] == '=':
                root1 = find(var1_index)
                root2 = find(var2_index)
                parent[root1] = root2

        for equation in equations:
            var1_index = ord(equation[0]) - ord('a')
            var2_index = ord(equation[-1]) - ord('a')
            if equation[1] == '!':
                if find(var1_index) == find(var2_index):
                    return False

        return True