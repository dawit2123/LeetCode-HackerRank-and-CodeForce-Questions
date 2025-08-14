# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    h = [0]*(N+1)
    for i in range(1, N+1):
        h[i] = int(next(it))

    INF = 10**18
    dp = [INF]*(N+1)
    dp[1] = 0

    for i in range(1, N):
        # jump to up to i+K
        limit = min(N, i + K)
        for j in range(i+1, limit+1):
            cost = abs(h[i] - h[j])
            if dp[j] > dp[i] + cost:
                dp[j] = dp[i] + cost

    print(dp[N])

if __name__ == "__main__":
    main()