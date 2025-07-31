# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter= {0:1}
        for n in nums:
            tmp={}
            for tot, count in counter.items():
                tmp[tot+n]= tmp.get(tot+n, 0)+count
                tmp[tot-n]= tmp.get(tot-n, 0)+count
            counter=tmp
        return counter.get(target, 0)