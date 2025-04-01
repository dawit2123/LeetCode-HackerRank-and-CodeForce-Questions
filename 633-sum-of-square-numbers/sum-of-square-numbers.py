class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # iterate over the number from 0 to  square root of c
        left=0
        right= int(c**0.5)
        while left<=right:
            result= left*left+ right*right
            if result==c:
                return True
            elif result<c:
                left+=1
            else:
                right-=1
        return False