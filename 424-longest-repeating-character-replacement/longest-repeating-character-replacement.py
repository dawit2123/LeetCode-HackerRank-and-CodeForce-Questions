class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_freq=defaultdict(int)
        res=0
        l=0
        for r in range(len(s)):
            count_freq[s[r]]+=1
            while (sum(count_freq.values())-max(count_freq.values()))>k:
                count_freq[s[l]]-=1
                l+=1
            res=max(res, r-l+1)
        return res
