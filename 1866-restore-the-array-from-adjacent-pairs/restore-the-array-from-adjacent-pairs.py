from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs):
        graph = defaultdict(list)
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        array_length = len(adjacentPairs) + 1
        restored_array = [0] * array_length

        for node, neighbors in graph.items():
            if len(neighbors) == 1:  
                restored_array[0] = node
                restored_array[1] = neighbors[0]
                break

        for i in range(2, array_length):
            current_neighbors = graph[restored_array[i - 1]]
            restored_array[i] = current_neighbors[0] if current_neighbors[1] == restored_array[i - 2] else current_neighbors[1]
        return restored_array