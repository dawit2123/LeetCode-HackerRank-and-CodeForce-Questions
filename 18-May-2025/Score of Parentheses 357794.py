# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score_stack = [0] 

        for parentheses in s:
            if parentheses == "(":
                score_stack.append(0)
            elif score_stack:
                last_score = score_stack.pop() 
                score_stack[-1] += max(1, last_score * 2)
        
        return score_stack[-1]