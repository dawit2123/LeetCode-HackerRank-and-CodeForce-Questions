class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_set=set(wordlist)
        small_letters_dict={}
        devowels_dict={}
        answers=[]
        def remove_vowels(word):
            temp=[]
            for char in word:
                if char in "aeiouAEIOU":
                    temp.append("*")
                else:
                    temp.append(char.lower())
            return "".join(temp)
        for word in wordlist:
            small_letter= word.lower()
            if small_letter not in small_letters_dict:
                small_letters_dict[small_letter]=word
            devowled_word= remove_vowels(word)
            if devowled_word not in devowels_dict:
                devowels_dict[devowled_word]=word
        # get the answers
        for query in queries:
            if query in words_set:
                answers.append(query)
                continue
            small_word= query.lower()
            if small_word in small_letters_dict:
                answers.append(small_letters_dict[small_word])
                continue
            devoweled_word= remove_vowels(query)
            if devoweled_word in devowels_dict:
                answers.append(devowels_dict[devoweled_word])
                continue
            answers.append("")
        return answers
        
        