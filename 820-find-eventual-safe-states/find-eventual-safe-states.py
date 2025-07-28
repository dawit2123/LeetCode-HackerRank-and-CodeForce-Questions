class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # define a hash map
        safe_map={}
        result=[]
        # write a dfs for all of them
        def dfs(i):
            if i in safe_map:
                return safe_map[i]
            safe_map[i]=False
            for neigh in graph[i]:
                if not dfs(neigh):
                    return False
            safe_map[i]=True
            return True
        for i in range(len(graph)):
            if dfs(i):
                result.append(i)
        return result