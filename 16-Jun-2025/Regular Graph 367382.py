# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

from collections import defaultdict
n, m = map(int, input().split())
degrees = [0] * (n + 1)
for _ in range(m):
    edge1, edge2 = map(int, input().split())
    degrees[edge1] += 1
    degrees[edge2] += 1
degree_values = degrees[1:]
if all(d == degree_values[0] for d in degree_values):
    print("YES")
else:
    print("NO")