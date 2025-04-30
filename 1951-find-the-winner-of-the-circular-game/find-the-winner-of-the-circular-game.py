class Solution(object):
    def findTheWinner(self, n, k):
        players = [x for x in range(1, n + 1)]
        remaining = n
        current_index = 0

        while remaining > 1:
            eliminated_index = (current_index + k - 1) % remaining
            players.pop(eliminated_index)
            current_index = eliminated_index
            remaining -= 1

        return players[0]