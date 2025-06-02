# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def combination(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total>target:
                return
            cur.append(candidates[i])
            combination(i, cur, total+candidates[i])
            cur.pop()
            combination(i+1, cur, total)
        combination(0,[],0)
        return res