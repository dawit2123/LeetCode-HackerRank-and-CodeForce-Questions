class Solution:
    def maxProduct(self, words: List[str]) -> int:
        num_words = len(words)
        masks = [0] * num_words
        for i, word in enumerate(words):
            for ch in word:
                masks[i] |= 1 << (ord(ch) - ord('a'))
      
        max_product = 0
        for i in range(num_words - 1):
            for j in range(i + 1, num_words):
                if masks[i] & masks[j] == 0:  
                    max_product = max(max_product, len(words[i]) * len(words[j]))                  
        return max_product