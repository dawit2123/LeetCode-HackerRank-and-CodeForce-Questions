class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack=[]
        for char in expression:
            if char in '(,':
                continue
            elif char in 'tf':
                stack.append(True if char == 't' else False)
            elif char in '&|!':
                stack.append(char)
            elif char == ')':
                operands = []
                
                while stack and (type(stack[-1]) is bool):
                    operands.append(stack.pop())
                operator = stack.pop()
                
                if operator == '&':
                    stack.append(all(operands))
                elif operator == '|':
                    stack.append(any(operands))
                elif operator == '!':
                    stack.append(not operands[0])
        
        return stack[-1]