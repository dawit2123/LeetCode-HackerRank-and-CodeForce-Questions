# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        total_min= 0
        tasks.sort()
        processorTime= sorted(processorTime)[::-1]
        temp=0
        for i in range(len(processorTime)):
            maximum_value=0
            for j in range(temp, temp+4):
                print(processorTime[i], tasks[j])
                maximum_value= max(maximum_value, processorTime[i]+tasks[j])
                temp+=1
            total_min= max(maximum_value, total_min)
        return total_min        
