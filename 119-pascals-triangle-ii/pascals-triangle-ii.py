class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [1]

        for i in range(1, rowIndex + 1):
            next_element = rows[i - 1] * (rowIndex - i + 1) // i
            rows.append(next_element)

        return rows