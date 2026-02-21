class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right= 0, len(matrix)-1
        while left<=right:
            mid=(left+right)//2
            if target>=matrix[mid][0] and target<=matrix[mid][-1]:
                l, r= 0, len(matrix[0])
                while l<=r:
                    m=(l+r)//2
                    if target==matrix[mid][m]:
                        return True
                    elif target<matrix[mid][m]:
                        r=m-1
                    else:
                        l=m+1
                return False
            elif target>matrix[mid][-1]:
                left=mid+1
            else:
                right=mid-1
        return False
