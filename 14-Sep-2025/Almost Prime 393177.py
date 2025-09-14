# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

import sys

MAX_N = 3000
num_distinct_prime_factors = [0] * (MAX_N + 1)

for p in range(2, MAX_N + 1):
    if num_distinct_prime_factors[p] == 0:
        for multiple in range(p, MAX_N + 1, p):
            num_distinct_prime_factors[multiple] += 1

n = int(sys.stdin.readline())

count_almost_primes = 0
for i in range(1, n + 1):
    if num_distinct_prime_factors[i] == 2:
        count_almost_primes += 1

sys.stdout.write(str(count_almost_primes) + "\n")