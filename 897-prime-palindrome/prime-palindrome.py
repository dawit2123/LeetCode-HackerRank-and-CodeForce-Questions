class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            divisor = 2
            while divisor * divisor <= x:
                if x % divisor == 0:
                    return False
                divisor += 1
            return True

        def reverse(x):
            result = 0
            while x:
                result = result * 10 + x % 10  
                x //= 10  
            return result

        while True:
            if reverse(n) == n and is_prime(n):
                return n
            if 10**7 < n < 10**8:
                n = 10**8
            n += 1