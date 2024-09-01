class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result=False
        for nums in matrix:
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=int((l+r)/2)
                if(target>nums[mid]):
                    l=mid+1
                elif(target<nums[mid]):
                    r=mid-1
                else:
                    return True
            result=False
        return result
        