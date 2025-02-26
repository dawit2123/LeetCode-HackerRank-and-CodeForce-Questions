# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set=set(allowed)
        words_set= [set(word) for word in words]
        result=0
        for word_set in words_set:
            if word_set<=allowed_set:
                result+=1
        return result