class Solution:
    def maxFreqSum(self, s: str) -> int:
        hash_map=Counter(s)
        max_vowel=0
        max_consonant=0
        vowels={"a", "e", "i", "o", "u"}
        for key in hash_map.keys():
            if key in vowels:
                max_vowel= max(max_vowel, hash_map[key])
            else:
                max_consonant= max(max_consonant, hash_map[key])
        return max_consonant+max_vowel