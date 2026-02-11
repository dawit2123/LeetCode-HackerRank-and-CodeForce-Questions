from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_count=defaultdict(int)
        result=0
        left=0
        max_freq=0
        for right in range(len(s)):
            s_count[s[right]]+=1
            max_freq= max(max_freq, s_count[s[right]])
            while (right-left+1) - max_freq>k:
                s_count[s[left]]-=1
                left+=1
            result=max(result, right-left+1)
        return result