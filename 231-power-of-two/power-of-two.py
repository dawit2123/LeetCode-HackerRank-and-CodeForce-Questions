class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0 and not(n&(n-1)):
            return True
        else:
            return False