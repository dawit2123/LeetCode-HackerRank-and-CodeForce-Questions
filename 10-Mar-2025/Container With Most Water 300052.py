# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount=0
        L=0
        R= len(height)-1
        while L<R:
            max_amount= max(max_amount,((R-L) * min(height[L], height[R])))
            print(max_amount)
            if height[L] <= height[R]:
                L+=1
            else:
                R-=1
        return max_amount
        