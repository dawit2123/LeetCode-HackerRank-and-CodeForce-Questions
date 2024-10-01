class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq=defaultdict(int)
        for num in arr:
            remainder=(num%k+k)%k
            freq[remainder]+=1
        for i in range(1, (k//2)+1):
            if freq[i]!=freq[k-i]:
                return False
        if freq[0]%2!=0:
            return False
        return True
        