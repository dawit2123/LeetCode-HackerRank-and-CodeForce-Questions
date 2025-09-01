class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # build it using max heap
        max_average_pass_sum=0
        max_heap= [(((num1/num2)-((num1+1)/(num2+1))),num1, num2) for num1, num2 in classes]
        heapq.heapify(max_heap)
        for _ in range(extraStudents):
            average_increase, num1, num2 = heapq.heappop(max_heap)
            num1+=1
            num2+=1
            heapq.heappush(max_heap, (((num1/num2)-((num1+1)/(num2+1))), num1, num2))
        max_average_pass_sum= sum(num1/num2 for _, num1, num2 in max_heap) 
        return max_average_pass_sum/len(classes)
