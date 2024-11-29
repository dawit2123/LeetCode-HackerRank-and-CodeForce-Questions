class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l=m=0
        res=0
        odds=0
        for r in range(len(nums)):
            if nums[r]%2:
                odds+=1
            while odds>k:
                if nums[l]%2:
                    odds-=1
                l+=1
                m=l
            if odds==k:
                while not nums[m]%2:
                    m+=1
                res=res+(m-l+1)
        return res