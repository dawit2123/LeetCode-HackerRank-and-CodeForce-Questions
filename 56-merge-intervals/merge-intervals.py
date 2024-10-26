class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            last=res[-1]
            cur=intervals[i]
            if last[1]>=cur[0]:
                last[1]=max(cur[1], last[1])
            else:
                res.append(cur)
        return res