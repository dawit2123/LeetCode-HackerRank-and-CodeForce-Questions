class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            
            for nei in adj[node]:
                if nei in visited:
                    continue
                queue.append(nei)
                visited.add(nei)
        return False
	