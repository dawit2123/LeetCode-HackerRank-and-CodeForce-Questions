class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        answer=[0]
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            if nums[i]<(nums[i-1]+nums[i-2]):
                print(nums[i], nums[i-1], nums[i-2])
                answer.append(nums[i]+nums[i-1]+nums[i-2])
                break

        return answer[-1]