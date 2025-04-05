# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic,res=dict(),0
        for i in answers:
            if i in dic:dic[i]+=1
            else:dic[i]=1
        for i,j in dic.items():
            if (j%(i+1))%(i+1)==0:res+=((j//(i+1))*(i+1))
            else:res+=(((j//(i+1))+1)*(i+1))
        return res