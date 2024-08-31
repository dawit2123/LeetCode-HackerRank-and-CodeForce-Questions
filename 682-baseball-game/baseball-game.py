class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for value in operations:
            if(value=="C"):
                stack.pop()
            elif(value=="D"):
                stack.append(stack[-1]*2)
            elif(value=="+"):
                stack.append(stack[-1]+ stack[-2])
            else:
                stack.append(int(value))
        return sum(stack)