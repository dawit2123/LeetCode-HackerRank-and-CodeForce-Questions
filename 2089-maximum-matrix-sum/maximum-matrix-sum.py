class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        smallest_num=float('inf')
        negative_count=0
        matrix_sum=0
        for i in range(n):
            for j in range(n):
                abs_val=abs(matrix[i][j])
                matrix_sum+=abs_val
                smallest_num=min(smallest_num, abs_val)
                if matrix[i][j]<0:
                    negative_count+=1
        if negative_count%2!=0:
           matrix_sum= (matrix_sum-(2*smallest_num))
        return matrix_sum
                
                