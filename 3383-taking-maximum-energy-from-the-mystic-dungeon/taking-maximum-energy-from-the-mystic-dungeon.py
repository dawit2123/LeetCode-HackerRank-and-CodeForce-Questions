class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        result=float('-inf')
        dp=[0]*len(energy)
        for i in range(len(energy)-1, -1, -1):
            dp[i]=energy[i]+(dp[i+k] if i+k<len(energy) else 0)
            result=max(dp[i], result)
        return result

