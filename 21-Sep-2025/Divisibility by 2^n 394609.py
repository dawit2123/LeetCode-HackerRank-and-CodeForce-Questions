# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

import sys

def count_twos_in_num(num):
    count = 0
    if num == 0:
        return 0
    while num > 0 and num % 2 == 0:
        count += 1
        num //= 2
    return count

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    current_twos = 0
    for x_val in a:
        current_twos += count_twos_in_num(x_val)

    if current_twos >= n:
        sys.stdout.write("0\n")
        continue

    extra_twos_per_op = []
    for i in range(1, n + 1):
        extra_twos_per_op.append(count_twos_in_num(i))

    extra_twos_per_op.sort(reverse=True)

    operations_count = 0
    for extra_twos in extra_twos_per_op:
        current_twos += extra_twos
        operations_count += 1
        if current_twos >= n:
            break

    if current_twos >= n:
        sys.stdout.write(str(operations_count) + "\n")
    else:
        sys.stdout.write("-1\n")