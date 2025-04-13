# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A

test_cases = int(input())
for _ in range(test_cases):
    s = input().strip() + '#'
    v = []
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i+1]:
            i += 2
        else:
            v.append(s[i])
            i += 1
    v.sort()
    res = sorted(set(v[1:])) if len(v) > 1 else []
    print(''.join(res))