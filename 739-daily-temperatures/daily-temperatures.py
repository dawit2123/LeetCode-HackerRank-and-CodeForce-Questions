class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and stack[-1][1]<n:
                stack_i, stack_v= stack.pop()
                result[stack_i]=i-stack_i
            stack.append((i, n))
        return result