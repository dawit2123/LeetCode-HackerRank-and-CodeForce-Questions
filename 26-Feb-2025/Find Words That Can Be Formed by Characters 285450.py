# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count= Counter(chars)
        result=0
        for word in words:
            word_count= Counter(word)
            is_good=True
            for key in word_count.keys():
                if word_count[key]>chars_count[key]:
                    is_good=False
            if is_good:
                result+=len(word)
        return result