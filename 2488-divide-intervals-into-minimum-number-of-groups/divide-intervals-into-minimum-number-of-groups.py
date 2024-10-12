class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        res=0
        groups=0
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        l, r=0, 0
        while l<len(start):
            if start[l]<=end[r]:
                groups+=1
                l+=1
            else:
                groups-=1
                r+=1
            res=max(res, groups)
        return res