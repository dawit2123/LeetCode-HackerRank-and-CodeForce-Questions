class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_dict=set(wordDict)
        cur=[]
        result=[]
        def backtrack(i):
            if i==len(s):
                result.append(" ".join(cur))
            for j in range(i, len(s)):
                if s[i:j+1] in word_dict:
                    cur.append(s[i:j+1])
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return result