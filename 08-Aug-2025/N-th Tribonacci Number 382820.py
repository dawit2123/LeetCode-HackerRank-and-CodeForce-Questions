# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci=[0]*38
        tribonacci[1], tribonacci[2]=1, 1
        for i in range(3, 38):
            tribonacci[i]= tribonacci[i-1]+tribonacci[i-2]+tribonacci[i-3]
        return tribonacci[n]
        