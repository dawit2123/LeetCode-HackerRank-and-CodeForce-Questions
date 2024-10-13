class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res= [0]+flowerbed+[0]
        print(res)
        for i in range(1, len(res)-1):
            if res[i-1]==0 and res[i]==0 and res[i+1]==0:
                res[i]=1
                n-=1
        return n<=0