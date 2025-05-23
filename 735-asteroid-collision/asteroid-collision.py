class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
                
            else:
                a=asteroids[i]
                while  stack and a != 0:
                    if stack[-1]<0 and a<0:
                        break
                    if abs(a)<abs(stack[-1]):
                        a=0
                    elif abs(a)>abs(stack[-1]):
                        stack.pop(-1)
                    elif abs(a)==abs(stack[-1]):
                        a=0
                        stack.pop(-1)
                if a!=0:
                    stack.append(a)
        return stack