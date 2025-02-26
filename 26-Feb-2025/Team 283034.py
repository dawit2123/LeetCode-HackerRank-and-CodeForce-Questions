# Problem: Team - https://codeforces.com/contest/231/problem/A

from collections import Counter
n= int(input())
number_of_problems_solved=0
for _ in range(n):
    solved_one= input()
    cnt= Counter(solved_one.split(" "))
    if cnt["1"]>=2:
        number_of_problems_solved+=1
print(number_of_problems_solved)