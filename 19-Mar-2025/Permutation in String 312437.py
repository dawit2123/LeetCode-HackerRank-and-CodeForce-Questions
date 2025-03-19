# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_count=defaultdict(int)
        s1_count=Counter(s1)
        l=0
        s2_count=Counter(s2[l:len(s1)-1])

        for r in range(len(s1)-1, len(s2)):
            s2_count[s2[r]]+=1

            if s2_count==s1_count:
                return True
            s2_count[s2[l]]-=1
            if s2_count[s2[l]]==0:
                del s2_count[s2[l]]
            l+=1
        return False