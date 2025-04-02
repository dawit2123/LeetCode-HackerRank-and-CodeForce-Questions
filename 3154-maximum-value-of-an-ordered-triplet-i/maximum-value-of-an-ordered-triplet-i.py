class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maximum_diff= answer= maximum_num=0
        for num in nums:
            answer= max(answer, maximum_diff* num)
            maximum_diff= max(maximum_diff , maximum_num-num)
            maximum_num= max(maximum_num, num)
        return answer