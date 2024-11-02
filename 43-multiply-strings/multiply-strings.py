class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        len_num1, len_num2= len(num1), len(num2)
        res= [0]* (len_num1+len_num2)
        # mulitpliying the digits in reverse order
        for i in range(len_num1-1, -1, -1):
            digit1=int(num1[i])
            for j in range(len_num2-1, -1, -1):
                digit2=int(num2[j])
                res[i+j+1]+=digit1*digit2
        for i in range(len_num1+len_num2-1,0,-1):
            res[i-1]+=res[i]//10
            res[i]%=10
        start_index= 0 if res[0]!=0 else 1
        return "".join(str(digit) for digit in res[start_index:])