class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        nums1_set, nums2_set= set(nums1), set(nums2)
        for num in nums1_set:
            if num in nums2_set:
                result.append(num)
        return result