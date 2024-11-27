class Solution:
    def reverseVowels(self, s: str) -> str:
        s=[s[i] for i in range(len(s))]
        l=0
        r=len(s)-1
        vowels={"a", "e", "i", "o", "u"}
        while l<r:
            if s[l].lower() in vowels and s[r].lower() in vowels:
                s[l], s[r]= s[r], s[l]
                l+=1
                r-=1
            elif s[l].lower() not in vowels:
                l+=1
            else:
                r-=1
        return "".join(s)
