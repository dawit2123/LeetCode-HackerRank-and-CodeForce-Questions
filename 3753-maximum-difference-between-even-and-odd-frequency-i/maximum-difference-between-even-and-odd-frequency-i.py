class Solution:
    def maxDifference(self, s: str) -> int:
        freq_count= Counter(s)
        max_freq, min_freq=0, float("inf")
        print(freq_count)
        for val in freq_count.values():
            if val>max_freq and val%2!=0:
                max_freq= val
            elif val<min_freq and val%2==0:
                min_freq= val
        return max_freq- min_freq