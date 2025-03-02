# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

result=[]
for _ in range(5):
    result.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if result[i][j]==1:
            print(abs(i-2)+abs(j-2))
            break