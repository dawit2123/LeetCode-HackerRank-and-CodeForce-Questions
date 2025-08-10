# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache=[0]*len(questions)
        def backtrack(i):
            if i>=len(questions):
                return 0
            point, power= questions[i]
            if cache[i]!=0:
                return cache[i]
            else:
                cache[i] = max(backtrack(i+1), point + backtrack(i+1+power))
                return cache[i]
        return backtrack(0)