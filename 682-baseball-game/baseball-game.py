class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for value in operations:
            if(value=="C"):
                stack.pop()
            elif(value=="D"):
                stack.append(int(stack[len(stack)-1])*2)
            elif(value=="+"):
                stack.append(int(stack[len(stack)-1])+ int(stack[len(stack)-2]))
            else:
                stack.append(value)
        sum=0
        for result in stack:
            sum+=int(result)
        return sum