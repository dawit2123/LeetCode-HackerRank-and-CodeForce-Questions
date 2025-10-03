from typing import List
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        if prerequisites == []:
            return [False] * len(queries)

        # changed: allow multiple parents
        parent = defaultdict(list)
        for u, v in prerequisites:
            parent[v].append(u)

        # changed: fixed dfs logic
        def dfs(c, target, seen):
            if c == target:       # reached target prerequisite
                return True
            for p in parent[c]:   # check all parents
                if p not in seen:
                    seen.add(p)
                    if dfs(p, target, seen):
                        return True
            return False

        ans = []
        for u, v in queries:
            ans.append(dfs(v, u, set()))

        return ans