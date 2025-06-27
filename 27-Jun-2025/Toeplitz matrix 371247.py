# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, m: List[List[int]]) -> bool:
        # compare each row to the next row shifted by 1 
        return all(m[r+1][1:] == m[r][:-1] for r in range(len(m)-1))