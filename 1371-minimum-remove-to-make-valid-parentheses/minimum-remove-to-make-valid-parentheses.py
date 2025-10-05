class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result=[]
        cnt=0
        for c in s:
            if c=="(":
                cnt+=1
                result.append(c)
            elif c==")" and cnt>0:
                result.append(c)
                cnt-=1
            elif c!=")":
                result.append(c)
        # check for the reverse one
        filtered=[]
        back_cnt=0
        for i in range(len(result)-1, -1, -1):
            if result[i]==")":
                filtered.append(result[i])
                back_cnt+=1
            elif result[i]=="(" and back_cnt>0:
                filtered.append(result[i])
                back_cnt-=1
            elif result[i]!="(":
                filtered.append(result[i])
        filtered=filtered[::-1]
        return "".join(filtered)

