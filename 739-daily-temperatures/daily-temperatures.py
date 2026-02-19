class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[] # index
        for i in range(len(temperatures)):
            t=temperatures[i]
            while stack and t>temperatures[stack[-1]]:
                j=stack.pop()
                result[j]=(i-j)
            stack.append(i)
        return result