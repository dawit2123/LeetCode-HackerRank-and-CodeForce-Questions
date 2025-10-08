# implementation using a SortedDict
from sortedcontainers import SortedDict
from collections import defaultdict
class Leaderboard:

    def __init__(self):
        self.players_score=defaultdict(int) #playerId->score
        self.scores_count= SortedDict() # score->player_count

    def addScore(self, playerId: int, score: int) -> None:
        old_score=self.players_score[playerId]
        if old_score in self.scores_count:
            self.scores_count[old_score]-=1
            if self.scores_count[old_score]==0:
                del self.scores_count[old_score]
        new_score=old_score+score
        self.players_score[playerId]=new_score
        self.scores_count[new_score]=self.scores_count.get(new_score, 0)+1

    def top(self, K: int) -> int:
        result=0
        for value in reversed(self.scores_count):
            takes= min(self.scores_count[value], K)
            result+=(value*takes)
            K-=takes
            if K==0:
                return result

    def reset(self, playerId: int) -> None:
        old_score= self.players_score[playerId]
        if old_score:
            self.scores_count[old_score]-=1
            if self.scores_count[old_score]==0:
                del self.scores_count[old_score]
        self.players_score[playerId]=0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)