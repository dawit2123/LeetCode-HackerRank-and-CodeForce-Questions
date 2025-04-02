class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result=0
        sum_map=defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                sum_map[num1+num2]+=1
        for num3 in nums3:
            for num4 in nums4:
                result+=sum_map[-(num3+num4)]
        return result