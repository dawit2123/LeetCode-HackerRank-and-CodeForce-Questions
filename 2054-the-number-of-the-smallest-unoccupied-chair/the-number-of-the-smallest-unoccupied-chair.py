class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times_modified= [(t[0], t[1], i) for i,t in enumerate(times)]
        times_modified.sort()
        used_chairs=[]
        available_chairs=[i for i in range(len(times_modified))]

        for a , l, i in times_modified:
            while used_chairs and used_chairs[0][0] <=a:
                leave, chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, chair)
            chair= heapq.heappop(available_chairs)
            heapq.heappush(used_chairs, (l,chair))
            if i==targetFriend:
                return chair
        return -1