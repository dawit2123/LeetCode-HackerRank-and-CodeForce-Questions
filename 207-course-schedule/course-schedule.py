class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for tar, src in prerequisites:
            print(tar, src)
            adj[src].append(tar)
        visit=set()
        path=set()
        for i in range(numCourses):
            if not self.dfs(i, adj, visit, path):
                return False
        return True
    def dfs(self, src, adj, visit, path):
        if src in path:
            return False
        if src in visit:
            return True
        visit.add(src)
        path.add(src)
        for neighbour in adj[src]:
            if not (self.dfs(neighbour, adj, visit, path)):
                return False
        path.remove(src)
        return True
        