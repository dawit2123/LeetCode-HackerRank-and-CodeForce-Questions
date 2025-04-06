# Problem: Arithmetic Progression - https://codeforces.com/problemset/problem/382/C

n = int(input())
cards = list(map(int, input().split()))
if n == 1:
    print(-1)
elif n == 2:
    a, b = sorted(cards)
    diff = b - a
    valid = [a - diff, b + diff]
    if (a + b) % 2 == 0:
        valid.append((a + b) // 2)
    valid = sorted(set(valid))
    print(len(valid))
    print(' '.join(map(str, valid)))
else:
    cards.sort()
    diffs = [cards[i+1] - cards[i] for i in range(n-1)]
    unique_diffs = set(diffs)
    if len(unique_diffs) > 2:
        print(0)
    elif len(unique_diffs) == 1:
        d = diffs[0]
        valid = [cards[0] - d, cards[-1] + d]
        valid = sorted(set(valid))
        print(len(valid))
        print(' '.join(map(str, valid)))
    else:
        sorted_diffs = sorted(unique_diffs)
        d1, d2 = sorted_diffs
        if d2 != 2 * d1:
            print(0)
        else:
            count_d1 = diffs.count(d1)
            count_d2 = diffs.count(d2)
            if count_d2 == 1 and count_d1 == (n-1 - count_d2):
                for i in range(n-1):
                    if diffs[i] == d2:
                        print(1)
                        print(cards[i] + d1)
                        exit()
                print(0)
            else:
                print(0)