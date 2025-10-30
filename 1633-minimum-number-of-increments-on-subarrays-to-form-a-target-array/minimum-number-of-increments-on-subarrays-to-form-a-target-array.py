class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if len(target)==0:
            return 0
        prev=0
        result=0
        for i in range(len(target)):
            if (target[i]-prev)>0:
                result+=(target[i]-prev)
            prev=target[i]
        return result