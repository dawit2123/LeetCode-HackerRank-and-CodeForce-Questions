class Solution:
    def sortVowels(self, s: str) -> str:
        t=[]
        vowels={"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        t_vowels=[]
        for char in s:
            if char in vowels:
                t.append("vowel")
                t_vowels.append(char)
            else:
                t.append(char)
        t_vowels=sorted(t_vowels)
        i=0
        for j in range(len(t)):
            if t[j]=="vowel":
                t[j]=t_vowels[i]
                i+=1
        return "".join(t)
        