class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        first_word_counter= Counter(words[0])
        for i in range(1, len(words)):
            word= Counter(words[i])
            for c in first_word_counter:
                first_word_counter[c]=min(first_word_counter[c], word[c])
        result=[]
        for word, count in first_word_counter.items():
            result.extend([word]*count)
        return result