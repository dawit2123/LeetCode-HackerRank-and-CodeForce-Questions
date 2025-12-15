class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices)<2:
            return len(prices)
        result=0
        left=0
        prices_len=len(prices)
        while left<prices_len:
            next_index=left+1
            while next_index<prices_len and prices[next_index]==prices[next_index-1]-1:
                next_index+=1
            n=next_index-left+1
            result+=int(((n*(n-1))/2))
            left=next_index
        return result