class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result= [[0]*len(matrix) for _ in range(len(matrix[0]))]
        ROW= len(matrix)
        COLS= len(matrix[0])
        for r in range(ROW):
            for c in range(COLS):
                result[c][r] = matrix[r][c]
        return result