# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
      obj_s=defaultdict(int)
      for i in range(len(s)):
        obj_s[s[i]]+=1
      for char in obj_s:
        if obj_s[char]==1:
            return s.index(char)
      return -1  