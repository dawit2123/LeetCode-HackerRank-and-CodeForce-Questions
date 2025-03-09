# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        is_negative, count_zeros, nums_string, nums= False, 0, str(num), []
        # edge case
        if num==0:
            return 0
        if nums_string[0]=="-":
            nums_string=nums_string[1:]
            is_negative=True
        
        for char in nums_string:
            if char!="0":
                nums.append(char)
            else:
                count_zeros+=1
        if is_negative:
            nums.sort(reverse=True)
            nums_string="".join(nums)
            return int("-"+nums_string[0:]+"0"*count_zeros)
        else:
            nums.sort()
            nums_string="".join(nums)
            return int(nums_string[0]+"0"*count_zeros+nums_string[1:])
        
        