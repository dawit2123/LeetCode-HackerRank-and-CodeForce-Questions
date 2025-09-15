class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words= text.split()
        broken_letters_set=set(brokenLetters)
        valid_words=0
        for word in words:
            is_valid=True
            for char in word:
                if char in broken_letters_set:
                    is_valid=False
                    break
            if is_valid:
                valid_words+=1
        return valid_words