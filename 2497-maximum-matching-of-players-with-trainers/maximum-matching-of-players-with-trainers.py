class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i=0
        count=0
        for j in range(len(trainers)):
            if i>=len(players):
                break
            if players[i]<=trainers[j]:
                count+=1
                i+=1
        return count