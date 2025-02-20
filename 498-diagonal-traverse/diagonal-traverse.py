class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows= len(mat)
        cols= len(mat[0])
        answer=[]
        temp=[[] for _ in range(rows+cols-1)]
        for r in range(rows):
            for c in range(cols):
                temp[r+c].append(mat[r][c])
        for diagonal in range(rows+cols-1):
            if diagonal%2==0:
                answer.extend(temp[diagonal][::-1])
            else:
                answer.extend(temp[diagonal])
        return answer