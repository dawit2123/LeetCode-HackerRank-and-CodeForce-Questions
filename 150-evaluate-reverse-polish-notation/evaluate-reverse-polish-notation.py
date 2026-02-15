class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators={"+","-","*","/"}
        stack=[]
        for token in tokens:
            if token in operators:
                number1=stack.pop()
                number2=stack.pop()
                if token=="+":
                    stack.append(number1+number2)
                elif token=="-":
                    stack.append(number2-number1)
                elif token=="*":
                    stack.append(number1*number2)
                elif token=="/":
                    stack.append(int((number2)/number1))
            else:
                stack.append(int(token))
        return stack[-1]