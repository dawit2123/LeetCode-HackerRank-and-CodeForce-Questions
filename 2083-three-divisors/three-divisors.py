class Solution:
    def isThree(self, n: int) -> bool:
        divisors_count=sum(n%d==0 for d in range(2, n))
        return divisors_count==1