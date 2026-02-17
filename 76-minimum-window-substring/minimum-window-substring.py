from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)==0:
            return ""
        t_count=Counter(t)
        s_count=defaultdict(int)
        have, need= 0, len(t_count)
        min_left, min_right, min_window= 0, 0, float('infinity')
        left=0
        for right in range(len(s)):
            c=s[right]
            if c in t_count:
                s_count[c]+=1
                if s_count[c]==t_count[c]:
                    have+=1
            while have==need:
                c=s[left]
                print('hello', min_left, min_right)
                if (right-left+1)<min_window:
                    min_left, min_right, min_window= left, right, (right-left+1)
                if c in t_count:
                    s_count[c]-=1
                    if s_count[c]<t_count[c]:
                        have-=1
                left+=1
        return s[min_left:min_right+1] if min_window!=float('infinity') else ""


