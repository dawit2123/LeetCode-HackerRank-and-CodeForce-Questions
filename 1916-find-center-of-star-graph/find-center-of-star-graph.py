class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first, second = edges[0], edges[1]

        return first[0] if first[0] in second else first[1]