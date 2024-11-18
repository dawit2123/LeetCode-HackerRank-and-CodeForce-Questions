class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph=defaultdict(list)
        self.result=[]
        for i , edges in enumerate(graph):
            self.graph[i]=edges
        def dfs(cur_list, cur_node):
            if cur_node==len(graph)-1:
                self.result.append(cur_list.copy())
                return
            for col in graph[cur_node]:
                cur_list.append(col)
                dfs(cur_list, col)
                cur_list.pop()
        dfs([0],0)
        return self.result
            