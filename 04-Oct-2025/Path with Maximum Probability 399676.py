# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjacents=defaultdict(list)
        for i in range(len(edges)):
            start, end = edges[i]
            adjacents[start].append((end, succProb[i]))
            adjacents[end].append((start, succProb[i]))

        probability=[(-1, start_node)]
        visit=set()
        while probability:
            prob1, node1= heapq.heappop(probability)
            visit.add(node1)
            if node1==end_node:
                return prob1*-1
            for node2, prob2 in adjacents[node1]:
                if node2 not in visit:
                    heapq.heappush(probability, ((prob1*prob2), node2))
        return 0
            