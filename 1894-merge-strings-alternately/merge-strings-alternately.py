class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        word1_length=len(word1)
        word2_length= len(word2)
        i=0
        while i<word1_length and i<word2_length:
            res+=(word1[i]+word2[i])
            i+=1
        if i<word1_length:
            res+=word1[i:]
        if i<word2_length:
            res+=word2[i:]
        return res

        