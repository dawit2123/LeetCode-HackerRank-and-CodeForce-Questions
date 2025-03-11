# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

from bisect import bisect_left
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans=[-1]*len(intervals)
        for index, interval in enumerate(intervals):
            interval.append(index)
        intervals.sort()
        for _, end, index in intervals:
            right_index= bisect_left(intervals, [end])
            if right_index<len(intervals):
                ans[index]= intervals[right_index][2]
        return ans
