class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s)<2:
            return False
        def recursion(digits):
            if len(digits)==2:
                if digits[0]==digits[1]:
                    return True
                else:
                    return False
            temp=""
            for i in range(len(digits)-1):
                temp+=str((int(digits[i])+int(digits[i+1]))%10)
            return recursion(temp)
        return recursion(s)
            