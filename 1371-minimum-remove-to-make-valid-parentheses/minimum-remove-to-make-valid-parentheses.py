class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result=[]
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                result.append(s[i])
                count+=1
            elif s[i]==")" and count>0:
                result.append(s[i])
                count-=1
            elif s[i]==")" and count<=0:
                continue
            else:
                result.append(s[i])
        temp=[]
        # iterate from the backward and remove the ( slashes
        for j in range(len(result)-1, -1, -1):
            if result[j]=="(" and count>0:
                count-=1
            else:
                temp.append(result[j])
        return "".join(temp[::-1])