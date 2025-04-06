# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

number_of_cards= int(input())
cards= list(map(int, input().split()))
sereja_total_point=dima_total_point=0
left, right= 0, len(cards)-1
is_sereja=True
is_dima=False
while left<=right: 
    if is_sereja:
        is_sereja=False
        is_dima=True
        if cards[left]>=cards[right]:
            sereja_total_point+=cards[left]
            left+=1
        else:
            sereja_total_point+=cards[right]
            right-=1
    else:
        is_dima=False
        is_sereja=True
        if cards[left]>=cards[right]:
            dima_total_point+=cards[left]
            left+=1
        else:
            dima_total_point+=cards[right]
            right-=1
print(sereja_total_point,dima_total_point)