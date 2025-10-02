# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        attributes={}
        for i in range(1, n+1):
            attributes[i]=[]
        # iterate over the times and fill in the attributes
        for s,d,w in times:
            attributes[s].append((d,w))
        time_travel_result={}
        #instantiate a min_heap
        min_heap=[(0,k)]
        while min_heap:
            w1, n1, = heapq.heappop(min_heap)
            if n1 in time_travel_result:
                continue
            time_travel_result[n1]=w1

            # add all the adjacents of the current into the min_heap
            for n2, w2 in attributes[n1]:
                if n2 not in time_travel_result:
                    heapq.heappush(min_heap, ((w2+w1), n2))
        return max(time_travel_result.values()) if len(time_travel_result)==n else -1