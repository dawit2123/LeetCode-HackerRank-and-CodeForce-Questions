class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
  
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
  
    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)
      
        if root_a == root_b:
            return False
      
        if self.size[root_a] > self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        else:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]
      
        return True


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        union_find = UnionFind(len(stones))
        successful_unions = 0
      
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones[:i]):
                if x1 == x2 or y1 == y2:
                    successful_unions += union_find.union(i, j)
      
        return successful_unions