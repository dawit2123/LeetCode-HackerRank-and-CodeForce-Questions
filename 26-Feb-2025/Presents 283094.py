# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n= int(input())
gifts= list(map(int, input().split()))
result=[0]*n
for i in range(n):
    result[gifts[i]-1]=i+1
print(" ".join(map(str, result)))