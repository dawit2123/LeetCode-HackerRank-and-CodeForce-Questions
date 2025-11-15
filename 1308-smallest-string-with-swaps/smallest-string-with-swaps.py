class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        adj_list = defaultdict(list)
        visited = [False] * n

        # Build adjacency list
        for i, j in pairs:
            adj_list[i].append(j)
            adj_list[j].append(i)

        # DFS function to explore connected components
        def dfs(vertex, characters, indices):
            characters.append(s[vertex])
            indices.append(vertex)

            for adjacent in adj_list[vertex]:
                if not visited[adjacent]:
                    visited[adjacent] = True
                    dfs(adjacent, characters, indices)

        result = [''] * n

        # Explore all components
        for vertex in range(n):
            if not visited[vertex]:
                visited[vertex] = True
                characters, indices = [], []
                dfs(vertex, characters, indices)

                # Sort and reassign smallest possible characters
                characters.sort()
                indices.sort()

                for i in range(len(indices)):
                    result[indices[i]] = characters[i]

        return ''.join(result)