class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        for i , word in enumerate(s_list):
            word= word[::-1]
            s_list[i]=word
        return " ".join(s_list)