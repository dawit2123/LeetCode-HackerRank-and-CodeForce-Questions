class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        while n > 1:
            # use the modulus operator to check if it's divisible by 4 using the logarithmic approach
            if n % 4 != 0:
                return False
            n //= 4

        return True        