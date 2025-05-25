from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = Counter(words)
        length_of_palindrome = central_letter_pair_count = 0
      
        for word, count in word_count.items():
            if word[0] == word[1]:
                central_letter_pair_count += count % 2
                length_of_palindrome += (count // 2) * 4
            else:
                length_of_palindrome += min(count, word_count[word[::-1]]) * 2      
        length_of_palindrome += 2 if central_letter_pair_count else 0
        return length_of_palindrome