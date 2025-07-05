from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        max_lucky_integer= float('-inf')
        frequency= Counter(arr)
        for key in frequency.keys():
            if key==frequency[key]:
                max_lucky_integer=max(max_lucky_integer, key)
        return max_lucky_integer if max_lucky_integer!=float('-inf') else -1