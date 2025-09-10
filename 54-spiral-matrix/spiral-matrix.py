class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right= 0, len(matrix[0])
        output=[]
        while left<right and top<bottom:
            # append the top
            for i in range(left, right):
                output.append(matrix[top][i])
            top+=1
            # append the right
            for j in range(top, bottom):
                output.append(matrix[j][right-1])
            right-=1
            if not(left<right and top<bottom):
                break
            # append the bottom
            print(right-1, left-1)
            for k in range(right-1, left-1, -1):
                output.append(matrix[bottom-1][k])
            bottom-=1
            # append the left
            for m in range(bottom-1, top-1, -1):
                output.append(matrix[m][left])
            left+=1
        return output
            