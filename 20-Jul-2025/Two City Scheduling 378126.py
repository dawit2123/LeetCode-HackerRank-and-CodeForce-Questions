# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n= len(costs)//2
        costs.sort(key= lambda x: x[0]-x[1])
        total_sum= sum(costs[i][0] for i in range(n))+ sum(costs[i][1] for i in range(n, 2*n))
        return total_sum