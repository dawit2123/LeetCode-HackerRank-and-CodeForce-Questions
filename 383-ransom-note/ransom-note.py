class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter=Counter(magazine)
        for i in range(len(ransomNote)):
            if magazine_counter[ransomNote[i]] and magazine_counter[ransomNote[i]]>0:
                magazine_counter[ransomNote[i]]-=1
            else:
                return False
        return True