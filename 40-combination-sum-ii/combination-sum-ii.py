class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def dfs(i, cur, total):
            if total==target:
                result.append(cur.copy())
                return 
            if i>=len(candidates) or total>target:
                return
            # include the current number
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            # skip the current number
            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return result