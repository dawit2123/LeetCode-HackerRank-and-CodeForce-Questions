class Solution:
    def reverseWords(self, s: str) -> str:
        striped_str=s.strip()
        s_list= striped_str.split()
        print(' '.join(s_list[::-1]))
        return ' '.join(s_list[::-1])