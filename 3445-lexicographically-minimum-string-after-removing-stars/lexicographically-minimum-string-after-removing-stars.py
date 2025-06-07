class Solution:
    def clearStars(self, s: str) -> str:
        from collections import defaultdict

        freq = defaultdict(list)
        a_ord = ord('a')

        for i, ch in enumerate(s):
            if ch == '*':
                for j in range(26):
                    if freq[chr(a_ord + j)]:
                        freq[chr(a_ord + j)].pop()
                        break
            else:
                freq[ch].append(i)

        keep = [False] * len(s)
        for indices in freq.values():
            for idx in indices:
                keep[idx] = True

        return ''.join(s[i] for i in range(len(s)) if keep[i])