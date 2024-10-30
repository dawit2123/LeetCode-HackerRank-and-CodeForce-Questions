class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_start_position):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target and is_start_position==True:
                    l=mid
                    while l>=0:
                        if nums[l]==target:
                            print('hello', l, nums[l], target)
                            l-=1
                        else:
                            break
                    return l+1
                if nums[mid]==target and is_start_position==False:
                    r=mid
                    while r<len(nums):
                        if nums[r]==target:
                            r+=1
                        else:
                            break
                    return r-1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        left_pos=binary_search(nums, target, True)
        right_pos=binary_search(nums, target, False)
        return [left_pos, right_pos]
        
        