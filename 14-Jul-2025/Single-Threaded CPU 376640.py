# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key= lambda k:k[0])
        result, min_heap= [], []
        time, i= tasks[0][0], 0
        while min_heap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i+=1
            if min_heap:
                proc_time, index= heapq.heappop(min_heap)
                result.append(index)
                time+=proc_time
            else:   
                time= tasks[i][0]
        return result



