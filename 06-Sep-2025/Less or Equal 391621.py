# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())

values = list(map(int, input().split()))

values.sort()

if k == 0:
    if n == 0:
        print(1)
    elif values[0] > 1:
        print(values[0] - 1)
    else:
        print("-1")

elif k > 0 and k <= n:
    if k == n:
        print(values[n - 1])
    elif values[k - 1] == values[k - 1 + (1 if k < n else 0)]:
        print("-1")
    else:
        print(values[k - 1])
else:
    print("-1")