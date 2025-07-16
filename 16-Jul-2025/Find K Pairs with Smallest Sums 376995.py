# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Store the result and the priority queue
        result, priority_list=[], []
        # Add each element and their sum in the queue
        for num1 in nums1:
            heapq.heappush(priority_list, [num1+nums2[0], 0])
        while k>0 and len(priority_list)>0:
            # Pop the values and add into the result
            s, index= heapq.heappop(priority_list)
            result.append([s-nums2[index], nums2[index]])
            # Add the next element of the minimum candidate into the priority queue 
            if index<len(nums2)-1:
                heapq.heappush(priority_list, [s-nums2[index]+nums2[index+1],index+1])
            k-=1
        return result

