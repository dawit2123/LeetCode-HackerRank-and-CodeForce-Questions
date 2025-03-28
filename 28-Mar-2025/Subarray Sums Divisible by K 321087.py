# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        prefix={0:1}
        temp_sum=0
        for num in nums:
            temp_sum+=num
            remain=temp_sum%k
            if remain in prefix:
                res+=prefix[remain]
            prefix[remain]=prefix.get(remain, 0)+1
        return res