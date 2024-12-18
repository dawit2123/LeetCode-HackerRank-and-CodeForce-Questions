class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        count=Counter(tasks)
        max_heap= [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        queue=deque()
        while max_heap or queue:
            time+=1
            if max_heap:
                cnt= 1+ heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(max_heap,queue.popleft()[0])
        return time
