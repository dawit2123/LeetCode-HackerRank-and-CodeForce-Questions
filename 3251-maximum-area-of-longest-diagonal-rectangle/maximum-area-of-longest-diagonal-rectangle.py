class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maximum_area=0
        longest_diagonal=0
        for x,y in dimensions:
            diagonal=sqrt(x**2 + y**2)
            if diagonal>longest_diagonal:
                longest_diagonal= diagonal
                maximum_area=(x*y)
            elif diagonal==longest_diagonal:
                maximum_area= max(maximum_area,(x*y))
        return maximum_area