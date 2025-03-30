# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        b2c = {}
        freq = {}
        clr = set()
        res = []

        for ball, color in queries:
            if ball in b2c:
                prev_color = b2c[ball]
                freq[prev_color] -= 1
                if freq[prev_color] == 0:
                    clr.remove(prev_color)

            b2c[ball] = color
            freq[color] = freq.get(color, 0) + 1
            clr.add(color)
            res.append(len(clr))

        return res