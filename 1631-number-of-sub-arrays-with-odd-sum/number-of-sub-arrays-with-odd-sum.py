class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even_count=0
        odd_count=0
        cur_sum=0
        res=0
        MOD=10**9+7
        for num in arr:
            cur_sum+=num
            if cur_sum%2==1:
                res= (res%MOD)+even_count+1
                odd_count+=1
            else:
                res= (res%MOD)+odd_count
                even_count+=1
        return res
