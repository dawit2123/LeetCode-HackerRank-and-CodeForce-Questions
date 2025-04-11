# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        target= Counter(p)
        counter_s= Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            cur_char=s[i]
            counter_s[cur_char]+=1
            if counter_s==target:
                res.append(i-len(p)+1)
            counter_s[s[i-len(p)+1]]-=1
            if counter_s[s[i-len(p)+1]]==0:
                del counter_s[s[i-len(p)+1]]
        return res