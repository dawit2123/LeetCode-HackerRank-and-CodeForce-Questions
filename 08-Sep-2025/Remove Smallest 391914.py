# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

test_cases= int(input())
while test_cases>0:
    n= int(input())
    a= list(map(int, input().split()))
    a.sort()
    is_valid="YES"
    for i in range(n-1):
        if (a[i+1]-a[i])>1:
            is_valid="NO"
            break
    print(is_valid)
    test_cases-=1