# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digit_to_chars={
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(i, cur):
            if len(cur)==len(digits):
                res.append(cur)
                return
            for c in digit_to_chars[digits[i]]:
                dfs(i+1, cur+c)
        if  digits:
            dfs(0,"")
        return res