class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res=[0]*len(score)
        place=1
        heap=[]
        for index, val in enumerate(score):
            heapq.heappush(heap, [-1*val, index])
        while heap:
            max_score, max_index= heapq.heappop(heap)
            if place==1:
                res[max_index]="Gold Medal"
            elif place==2:
                res[max_index]="Silver Medal"
            elif place==3:
                res[max_index]="Bronze Medal"
            else:
                res[max_index]=str(place)
            place+=1
        return res