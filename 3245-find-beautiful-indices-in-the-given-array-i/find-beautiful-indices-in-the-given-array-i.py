class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ans = []
        indices_a, indices_b = [], []        
        for i in range(len(s) - len(a) + 1):
            if s[i:i+len(a)] == a:
                indices_a.append(i)        
        for j in range(len(s) - len(b) + 1):
            if s[j:j+len(b)] == b:
                indices_b.append(j)        
        for i in indices_a:
            for j in indices_b:
                if abs(i - j) <= k:
                    ans.append(i)
                    break        
        ans.sort()        
        return ans
