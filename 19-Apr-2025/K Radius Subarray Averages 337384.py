# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution(object):  
    def getAverages(self, values, radius):  
        length = len(values)  
        averages = [-1] * length  
        if length < radius * 2 + 1:  
            return averages  
        window_sum = sum(values[:2*radius+1])  
        averages[radius] = window_sum // (2*radius + 1)  
        for idx in range(radius + 1, length - radius):  
            window_sum += (values[idx + radius] - values[idx - radius - 1])  
            averages[idx] = window_sum // (2*radius + 1)  
        return averages  