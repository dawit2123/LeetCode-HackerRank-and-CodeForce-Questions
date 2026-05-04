class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right= 0, len(matrix)-1
        while left<right:
            top,bottom= left, right
            for i in range(right-left):
                # get the value of trhe top left
                top_left= matrix[top][left+i]
                # put the value of the bottom left to the top left
                matrix[top][left+i]=matrix[bottom-i][left]
                # put the value of the bottom right to the bottom left
                matrix[bottom-i][left]= matrix[bottom][right-i]
                # put the value of the top right into the bottom right
                matrix[bottom][right-i]=matrix[top+i][right]
                # put the top left to the top right
                matrix[top+i][right]=top_left
            left+=1
            right-=1
