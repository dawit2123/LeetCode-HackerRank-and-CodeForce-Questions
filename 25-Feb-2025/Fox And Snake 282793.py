# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

row, column= list(map(int, input().split()))
is_last=True
for i in range(row):
    if i%2==0:
        print("#"*column)
    else:
        if is_last:
            print("."*(column-1)+"#")
            is_last=False
        else:
            print("#"+"."*(column-1))
            is_last=True