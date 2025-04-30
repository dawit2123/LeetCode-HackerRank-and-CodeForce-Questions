class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num_of_even_number_of_digits=0
        for num in nums:
            count=0
            while num!=0:
                count+=1
                num= num//10
            if count%2==0:
                num_of_even_number_of_digits+=1
        return num_of_even_number_of_digits