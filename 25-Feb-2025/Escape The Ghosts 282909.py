# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        target_x, target_y= target
        return all(
            (abs(target_x-ghost_x)+abs(target_y-ghost_y))>(abs(target_x)+abs(target_y)) for ghost_x, ghost_y in ghosts
            )