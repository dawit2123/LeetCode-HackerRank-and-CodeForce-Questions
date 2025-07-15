class Solution:
    def isValid(self, word: str) -> bool:
        vowels= set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        is_consonant=False
        is_vowel=False
        if len(word)>=3:
            for c in word:
                if c.isalnum():
                    if not c.isdigit() and c in vowels:
                        is_vowel=True
                    elif not c.isdigit() and c not in vowels:
                        is_consonant=True
                else:
                    return False
            return is_vowel and is_consonant
        else:
            return False