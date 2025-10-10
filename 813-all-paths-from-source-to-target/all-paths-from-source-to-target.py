class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph_path= {}
        for i, edges in enumerate(graph):
            graph_path[i]=edges
        result=[]
        def dfs(i, cur):
            if i==(len(graph))-1:
                result.append(cur.copy())
            for direction in graph_path[i]:
                cur.append(direction)
                dfs(direction, cur)
                cur.pop()
        dfs(0, [0])
        return result