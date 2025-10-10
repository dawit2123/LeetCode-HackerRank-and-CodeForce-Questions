# Problem: Count Cells in Overlapping Horizontal and Vertical Substrings - https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/description/

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:

        def kmp_prefix(pattern):
            pref, k = [0], 0
            for i in range(1, len(pattern)):
                while k and pattern[k] != pattern[i]:
                    k = pref[k-1]
                if pattern[k] == pattern[i]:
                    k += 1
                pref.append(k)
            return pref

        def KMP(s, pattern, pref):
            k, nn, intervals = 0, len(pattern), []
            for right, ch in enumerate(s):
                while k > 0 and pattern[k] != ch:
                    k = pref[k-1]
                if pattern[k] == ch:
                    k += 1
                if k == nn:
                    left = right - nn + 1
                    if intervals and intervals[-1][1] >= left:
                        intervals[-1][1] = right
                    else:
                        intervals.append([left, right])
                    k = pref[k-1]
            return intervals

        
        m, n = len(grid), len(grid[0])
        pref = kmp_prefix(pattern)
        used = [0] * (m * n)
        for l, r in KMP(chain(*grid), pattern, pref):
            used[l:r+1] = [1] * (r-l+1)
        ans = 0
        for l, r in KMP(chain(*zip(*grid)), pattern, pref):
            ans += sum(used[i%m*n + i//m%n] for i in range(l, r+1))
        return ans