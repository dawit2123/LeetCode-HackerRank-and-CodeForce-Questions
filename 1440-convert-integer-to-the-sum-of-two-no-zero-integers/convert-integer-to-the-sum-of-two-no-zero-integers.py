class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def zero_checker(num):
            num_str= str(num)
            if "0" in num_str:
                return False
            else:
                return True
        for i in range(n):
            if zero_checker(i) and zero_checker(n-i):
                return [i, n-i]
        