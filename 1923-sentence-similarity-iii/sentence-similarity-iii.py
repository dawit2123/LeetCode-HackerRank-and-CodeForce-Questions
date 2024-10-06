class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
       word1, word2= sentence1.split(), sentence2.split()
       len_word1, len_word2 = len(word1), len(word2)
    
       if len_word2 < len_word1:
        word2, word1 = word1, word2
        len_word2, len_word1 = len_word1, len_word2

       start_word_count = end_word_count =0
       while start_word_count<len_word1 and word1[start_word_count]==word2[start_word_count]:
            start_word_count+=1
       while end_word_count< len_word1 and word1[len_word1-1-end_word_count] == word2[len_word2-1-end_word_count]:
            end_word_count+=1
       return start_word_count+end_word_count>=len_word1 