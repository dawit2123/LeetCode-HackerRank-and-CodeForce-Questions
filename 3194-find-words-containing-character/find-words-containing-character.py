class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for i in range(len(words)):
            for c in words[i]:
                if c==x:
                    result.append(i)
                    break
        return result