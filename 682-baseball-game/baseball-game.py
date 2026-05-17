class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        total_sum=0
        for operation in operations:
            if operation == "+":
                value=stack[-1]+stack[-2]
                stack.append(value)
                total_sum+=value
            elif operation == "C":
                value=stack.pop()
                total_sum-=value
            elif operation == "D":
                value=2*stack[-1]
                stack.append(value)
                total_sum+=value
            else:
                value=int(operation)
                stack.append(value)
                total_sum+=value
        return total_sum