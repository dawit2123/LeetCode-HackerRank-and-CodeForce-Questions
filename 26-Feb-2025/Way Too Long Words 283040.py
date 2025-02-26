# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n= int(input())
for _ in range(n):
    word= input()
    length_of_word= len(word)
    if length_of_word>10:
        print(word[0]+str(length_of_word-2)+word[length_of_word-1])
    else:
        print(word)