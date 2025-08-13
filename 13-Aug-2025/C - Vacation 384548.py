# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    a = [0]*(N+1)
    b = [0]*(N+1)
    c = [0]*(N+1)
    for i in range(1, N+1):
        a[i] = int(next(it))
        b[i] = int(next(it))
        c[i] = int(next(it))

    # dp for previous day
    dpA = a[1]
    dpB = b[1]
    dpC = c[1]

    for i in range(2, N+1):
        newA = a[i] + max(dpB, dpC)
        newB = b[i] + max(dpA, dpC)
        newC = c[i] + max(dpA, dpB)
        dpA, dpB, dpC = newA, newB, newC

    print(max(dpA, dpB, dpC))

if __name__ == "__main__":
    main()