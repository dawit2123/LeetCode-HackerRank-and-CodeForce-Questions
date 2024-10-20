class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack=[]
        for char in expression:
            if char == ',':
                continue
            elif char in 'tf':
                # Push True for 't' and False for 'f'
                stack.append(True if char == 't' else False)
            elif char in '(&|!':
                # Push the operator onto the stack
                stack.append(char)
            elif char == ')':
                # We've reached the end of an expression, process it
                operands = []
                
                # Pop the stack until we find the operator
                while stack and (type(stack[-1]) is bool):
                    operands.append(stack.pop())
                stack.pop()
                operator = stack.pop()
                
                if operator == '&':
                    # AND: return True only if all operands are True
                    stack.append(all(operands))
                elif operator == '|':
                    # OR: return True if any operand is True
                    stack.append(any(operands))
                elif operator == '!':
                    # NOT: only one operand is expected, negate it
                    stack.append(not operands[0])
        
        # The final result will be the only item left on the stack
        return stack[-1]