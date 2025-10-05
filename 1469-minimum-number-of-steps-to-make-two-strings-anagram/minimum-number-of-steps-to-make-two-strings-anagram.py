class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count, t_count= Counter(s), Counter(t)
        result=0
        for key in s_count:
            if key in t_count:
                temp=s_count[key]-t_count[key]
                if temp>0:
                    result+=temp
            else:
                result+=(s_count[key])
        return result