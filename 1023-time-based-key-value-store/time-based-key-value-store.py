from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash_map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left, right= 0, len(self.hash_map[key])-1
        while left<=right:
            mid= (left+right)//2
            t=self.hash_map[key][mid][0]
            if t==timestamp:
                return self.hash_map[key][mid][1]
            elif t>timestamp:
                right=mid-1
            else:
                left=mid+1
        if left==0:
            return ""
        return self.hash_map[key][left-1][1]