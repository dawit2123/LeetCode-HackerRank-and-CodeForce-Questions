class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(dict)
        for i in range(len(equations)):
            x,y=equations[i]
            result=values[i]
            graph[x][y]=result
            graph[y][x]=1.0/result
        def dfs(x, y, visited):
            # if x not in graph or y not in graph:
            #     return -1

            if y in graph[x]:
                return graph[x][y]
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp=dfs(i, y, visited)
                    if temp==-1:
                        continue
                    else:
                        return graph[x][i]*temp
            return -1
        result=[] 
        for query in queries:
            result.append(dfs(query[0], query[1], set()))
        return result