# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """ My approach
        initialise the nums even sum
        go over the queries and if the existing one is even remove it, and if the updated one is even add into it and then append into the result  and manipulate it
        """
        even_sums=0
        answer=[]
        for num in nums:
            if num%2==0:
                even_sums+=num
        for query in queries:
            val, index= query
            if nums[index]%2==0:
                even_sums-=nums[index]
            nums[index]+=val
            if nums[index]%2==0:
                even_sums+=nums[index]
            answer.append(even_sums)
        return answer
