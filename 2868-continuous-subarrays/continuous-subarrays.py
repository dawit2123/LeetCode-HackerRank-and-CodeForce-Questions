from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        min_table = self.build_min_table(nums)
        max_table = self.build_max_table(nums)

        result = 0
        for i in range(n):
            low, high = i, n - 1

            while low < high:
                mid = (low + high + 1) // 2
                min_val = self.query(min_table, i, mid)
                max_val = self.queryMax(max_table, i, mid)

                if max_val - min_val > 2:
                    high = mid - 1
                else:
                    low = mid

            result += high - i + 1
        return result

    def lg2(self, x):
        return -1 if x == 0 else (x.bit_length() - 1)

    def build_min_table(self, a):
        n = len(a)
        max_k = self.lg2(n) + 1
        min_table = [[0] * n for _ in range(max_k)]

        for i in range(n):
            min_table[0][i] = a[i]

        for k in range(1, max_k):
            for i in range(n - (1 << k) + 1):
                min_table[k][i] = min(min_table[k - 1][i], min_table[k - 1][i + (1 << (k - 1))])
        return min_table

    def build_max_table(self, a):
        n = len(a)
        max_k = self.lg2(n) + 1
        max_table = [[0] * n for _ in range(max_k)]

        for i in range(n):
            max_table[0][i] = a[i]

        for k in range(1, max_k):
            for i in range(n - (1 << k) + 1):
                max_table[k][i] = max(max_table[k - 1][i], max_table[k - 1][i + (1 << (k - 1))])
        return max_table

    def query(self, table, x, y):
        k = self.lg2(y - x + 1)
        return min(table[k][x], table[k][y - (1 << k) + 1])

    def queryMax(self, table, x, y):
        k = self.lg2(y - x + 1)
        return max(table[k][x], table[k][y - (1 << k) + 1])