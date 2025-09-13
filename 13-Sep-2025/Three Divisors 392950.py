# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        divisors_count=sum(n%d==0 for d in range(2, n))
        return divisors_count==1