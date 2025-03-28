# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS,COLS= len(matrix), len(matrix[0])
        self.sum_matrix= [[0]*(COLS+1) for r in range(ROWS+1)]
        for R in range(ROWS):
            prefix=0
            for C in range(COLS):
                prefix+=matrix[R][C]
                above=self.sum_matrix[R][C+1]
                self.sum_matrix[R+1][C+1]=prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2= row1+1, row2+1, col1+1, col2+1
        upper= self.sum_matrix[row1-1][col2]
        left=self.sum_matrix[row2][col1-1]
        top_left=self.sum_matrix[row1-1][col1-1]
        bottom_right=self.sum_matrix[row2][col2]
        return bottom_right-upper-left+top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)