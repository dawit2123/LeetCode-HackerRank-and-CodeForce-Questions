class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for value in operations:
            print(f"stack", stack)
            if(value=="C"):
                stack.pop()
            elif(value=="D"):
                stack.append(int(stack[len(stack)-1])*2)
            elif(value=="+"):
                stack.append(int(stack[len(stack)-1])+ int(stack[len(stack)-2]))
            else:
                stack.append(value)
        print(f"stack {stack}")
        sum=0
        for result in stack:
            sum+=int(result)
        return sum