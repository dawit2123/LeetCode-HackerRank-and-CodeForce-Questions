class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in count(1):
            target=num1-k*num2
            if target<0:
                break
            if target.bit_count()<=k<=target:
                return k
        return -1