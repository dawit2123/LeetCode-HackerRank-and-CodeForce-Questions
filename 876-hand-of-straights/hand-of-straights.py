class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count={}
        for integer in hand:
            count[integer]= count.get(integer, 0)+1
        min_heap= list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first= min_heap[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True
