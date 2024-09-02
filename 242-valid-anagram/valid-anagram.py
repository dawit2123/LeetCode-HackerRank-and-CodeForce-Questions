class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj_s,obj_t={},{}
        if(len(s)!=len(t)):
            return False
        for i in range(0,len(s)):
            obj_s[s[i]]=1+obj_s.get(s[i],0)
            obj_t[t[i]]=1+obj_t.get(t[i],0)
        return True if obj_s==obj_t else False
        