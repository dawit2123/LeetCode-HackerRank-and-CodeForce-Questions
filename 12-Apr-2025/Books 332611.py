# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t= list(map(int, input().split()))
n_integers= list(map(int, input().split()))
n_integers.sort()
number_of_books=0
for i in range(len(n_integers)):
    if t>=n_integers[i]:
        number_of_books+=1
        t-=n_integers[i]
print(number_of_books)