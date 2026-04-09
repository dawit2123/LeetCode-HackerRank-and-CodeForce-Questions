from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash_map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        key_values= self.hash_map[key]
        left, right= 0, len(key_values)-1
        while left<=right:
            mid=(left+right)//2
            if key_values[mid][0]==timestamp:
                return key_values[mid][1]
            elif timestamp>key_values[mid][0]:
                left=mid+1
            else:
                right=mid-1
        if left==0:
            return ""
        return key_values[left-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)