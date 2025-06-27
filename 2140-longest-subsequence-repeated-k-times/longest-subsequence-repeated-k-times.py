class Solution:
    def longestSubsequenceRepeatedK(self, s: str, K: int) -> str:
        n = len(s)
        nextPos = [[n] * 26 for _ in range(n + 2)]

        for c in range(26):
            nextPos[n][c] = nextPos[n + 1][c] = n

        for i in range(n - 1, -1, -1):
            for c in range(26):
                nextPos[i][c] = nextPos[i + 1][c]
            nextPos[i][ord(s[i]) - ord('a')] = i

        low, high = 1, n // K
        res = ""

        while low <= high:
            mid = (low + high) // 2

            found = self.dfsTry(mid, K, 0, [''] * mid, s, nextPos)
            if found:
                res = found
                low = mid + 1
            else:
                high = mid - 1

        return res

    def dfsTry(self, length, K, idx, path, s, nextPos):
        if idx == length:
            return ''.join(path) if self.canExtend(path, length, s, nextPos, K) else None

        for c in reversed(range(26)):
            path[idx] = chr(ord('a') + c)

            if self.canExtend(path, idx + 1, s, nextPos, K):
                result = self.dfsTry(length, K, idx + 1, path, s, nextPos)
                if result:
                    return result

        return None

    def canExtend(self, path, d, s, nextPos, K):
        pos = 0
        n = len(s)

        for _ in range(K):
            for i in range(d):
                c = ord(path[i]) - ord('a')
                if pos >= n:
                    return False
                pos = nextPos[pos][c]
                if pos == n:
                    return False
                pos += 1
        return True