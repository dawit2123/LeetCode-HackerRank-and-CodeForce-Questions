class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        res=0
        sum=skill[0]+skill[j]
        while i<j:
            if skill[i]+skill[j]==sum:
                res+=skill[i]*skill[j]
                i+=1
                j-=1
            else:
                return -1
        return res
        