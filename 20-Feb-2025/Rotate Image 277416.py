# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right= 0, len(matrix)-1
        while left<right:
            top, bottom = left, right
            for i in range(right-left):
                # saving the top left
                top_left= matrix[top][left+i]

                # assigning the bottom left to the top left
                matrix[top][left+i]=matrix[bottom-i][left]

                # assigning the bottom right to bottom left
                matrix[bottom-i][left]= matrix[bottom][right-i]
                
                # assigning the top right to the bottom right
                matrix[bottom][right-i]= matrix[top+i][right]

                # assinging the top left to the top right
                matrix[top+i][right]= top_left
            left+=1
            right-=1