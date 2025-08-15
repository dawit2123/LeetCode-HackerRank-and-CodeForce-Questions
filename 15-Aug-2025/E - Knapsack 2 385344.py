# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

import sys

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    it = iter(data)
    N = next(it)
    W = next(it)
    w = []
    v = []
    sumV = 0
    for _ in range(N):
        wi = next(it)
        vi = next(it)
        w.append(wi)
        v.append(vi)
        sumV += vi

    INF = 10**18
    dp = [INF] * (sumV + 1)
    dp[0] = 0

    for i in range(N):
        for g in range(sumV - v[i], -1, -1):
            if dp[g] != INF:
                dp[g + v[i]] = min(dp[g + v[i]], dp[g] + w[i])

    ans = 0
    for g in range(sumV + 1):
        if dp[g] <= W:
            ans = g
    print(ans)

if __name__ == "__main__":
    main()