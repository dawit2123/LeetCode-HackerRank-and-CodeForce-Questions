# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    h = [0] + data[1:1+n]  

    if n == 2:
        print(abs(h[2] - h[1]))
        return

    dp1 = 0                 
    dp2 = abs(h[2] - h[1])  

    for i in range(3, n + 1):
        dpi = min(dp2 + abs(h[i] - h[i - 1]),
                  dp1 + abs(h[i] - h[i - 2]))
        dp1, dp2 = dp2, dpi

    print(dp2)

if __name__ == "__main__":
    main()