class Solution:
    def primePalindrome(self, n: int) -> int:
        # Helper function to check if a number is prime.
        def is_prime(x):
            if x < 2:
                return False
            divisor = 2
            # Check divisors up to the square root of x.
            while divisor * divisor <= x:
                if x % divisor == 0:
                    return False
                divisor += 1
            return True

        # Helper function to reverse an integer number.
        def reverse(x):
            result = 0
            while x:
                result = result * 10 + x % 10  # Add the last digit of x to result.
                x //= 10  # Remove the last digit of x.
            return result

        # Loop until we find the palindrome prime.
        while True:
            # Check if the number is both a palindrome and prime.
            if reverse(n) == n and is_prime(n):
                return n
            # Skip all numbers between 10^7 and 10^8, as there are no 8-digit palindrome primes.
            if 10**7 < n < 10**8:
                n = 10**8
            n += 1