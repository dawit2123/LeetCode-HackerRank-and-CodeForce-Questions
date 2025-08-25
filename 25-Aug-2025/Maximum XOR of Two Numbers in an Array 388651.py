# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # initializing the ans variable
        ans=0
        # build a prefix for a numbers from 32 to 1
        for i in range(31, -1, -1):
            ans<<=1
            prefix={num>>i for num in nums}
            target=ans^1
            can_set_bit= any((target^p) in prefix for p in prefix)
            ans+=1 if can_set_bit else 0
        return ans
        