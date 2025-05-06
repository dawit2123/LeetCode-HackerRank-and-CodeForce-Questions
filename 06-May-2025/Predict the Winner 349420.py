# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        arr1 = [0] * (n:= len(nums))
        for i in range(n-1,-1,-1):
            arr1[i] = nums[i]
            for j in range(i+1, n):
                arr1[j] = max(nums[i]-arr1[j  ],
                             nums[j]-arr1[j-1])
        return arr1[n-1] >= 0