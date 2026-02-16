class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_count, s2_count= [0]*26, [0]*26
        for c in s1:
            s1_count[ord(c)-ord('a')]+=1
        left=0
        for i in range(left, len(s1)-1):
            s2_count[ord(s2[i])-ord('a')]+=1
        for j in range(len(s1)-1, len(s2)):
            s2_count[ord(s2[j])-ord('a')]+=1
            if s2_count==s1_count:
                return True
            s2_count[ord(s2[left])-ord('a')]-=1
            left+=1
        return False