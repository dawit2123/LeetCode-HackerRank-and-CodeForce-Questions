class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        nums=list(enumerate(nums))
        def merge_list(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=merge_list(nums[:mid])
            right=merge_list(nums[mid:])
            return merge(left, right)
        def merge(left, right):
            l,r=0,0
            res=[]
            while l<len(left) or r<len(right):
                if r>=len(right) or (l<len(left) and left[l][1]<=right[r][1]):
                    result[left[l][0]]+=r
                    res.append(left[l])
                    l+=1
                else:
                    res.append(right[r])
                    r+=1
            return res
        merge_list(nums)
        return result