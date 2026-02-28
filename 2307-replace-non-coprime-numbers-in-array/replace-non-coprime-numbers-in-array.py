from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        for num in nums:
            stack.append(num)
            while len(stack)>1:
                second_last, last= stack[-2:]
                gcd_result= gcd(second_last, last)
                if gcd_result==1:
                    break
                stack.pop()
                stack[-1]= (second_last*last)//gcd_result
        return stack