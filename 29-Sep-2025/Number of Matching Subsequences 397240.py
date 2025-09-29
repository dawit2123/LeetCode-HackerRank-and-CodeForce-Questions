# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

from collections import defaultdict, deque
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting_dict = defaultdict(deque)
      
        for word in words:
            waiting_dict[word[0]].append(word)
      
        matching_count = 0
      
        for char in s:
            current_queue_size = len(waiting_dict[char])
            for _ in range(current_queue_size):
                current_word = waiting_dict[char].popleft()
                if len(current_word) == 1:
                    matching_count += 1
                else:
                    next_char = current_word[1]
                    remaining_word = current_word[1:]
                    waiting_dict[next_char].append(remaining_word)
      
        return matching_count