class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_count, s2_count= [0]*26, [0]*26
        for c in s1:
            s1_count[ord(c)-ord('a')]+=1
        for i in range(len(s1)-1):
            s2_count[ord(s2[i])-ord('a')]+=1
        left=0
        for right in range(len(s1)-1, len(s2)):
            s2_count[ord(s2[right])-ord('a')]+=1
            if s2_count==s1_count:
                return True
            else:
                s2_count[ord(s2[left])-ord('a')]-=1
                left+=1
        return False