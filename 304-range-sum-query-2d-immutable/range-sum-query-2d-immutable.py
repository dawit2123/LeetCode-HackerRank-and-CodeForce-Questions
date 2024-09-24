class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.rows_sum=[]
        for arr in self.matrix:
            val=[]
            res=0
            for num in arr:
                res+=num
                val.append(res)
            self.rows_sum.append(val)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result=0
        for numbers in range(row1, row2+1):
            left_prefix=self.rows_sum[numbers][col1-1] if col1>0 else 0
            right_prefix=self.rows_sum[numbers][col2]
            sum=right_prefix-left_prefix
            result+=sum
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)