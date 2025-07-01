class Solution:
    def possibleStringCount(self, word: str) -> int:
        length=1
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                length+=1
        return length