import heapq  

class Solution:  
    def longestDiverseString(self, a: int, b: int, c: int) -> str:  
        res = ""  
        max_heap =[]
        for i, c in [[a,"a"], [b, "b"], [c, "c"]]:
            if i!=0:
                max_heap.append([-i, c])
        heapq.heapify(max_heap)  
        prev = None
        while len(max_heap)>0:  
            val, char = heapq.heappop(max_heap)   
            val = -1 * val  
            req_char= min(2, val)
            print(prev, val)
            if prev and prev[0]>val:
                req_char= min(1, val)
            res+=char*req_char
            if prev and val > 0:  
                heapq.heappush(max_heap, [-prev[0], prev[1]])  
                prev=None
            val-=req_char
            prev = [val, char] if val > 0 else [0, ""]  
        return res