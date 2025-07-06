# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n= int(input())
integers= list(map(int, input().split()))
has_odd = False
has_even = False

for num in integers:
    if num % 2 == 0 and not has_even:
        has_even = True
    elif num % 2 == 1 and not has_odd:
        has_odd = True
    
    if has_odd and has_even:
        integers.sort()
        break
print(*integers)