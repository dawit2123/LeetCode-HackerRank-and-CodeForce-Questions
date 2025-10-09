class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start= sorted([intervals[i][0] for i in range(len(intervals))])
        end= sorted([intervals[i][1] for i in range(len(intervals))])
        s, e= 0, 0
        res, count=0, 0
        while s<len(start):
            if start[s]<end[e]:
                count+=1
                res= max(count, res)
                s+=1
            else:
                count-=1
                e+=1
        return res
