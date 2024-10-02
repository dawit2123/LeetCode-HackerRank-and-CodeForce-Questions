class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_nums=sorted(set(arr))
        ranks={}
        for i, num in enumerate(unique_nums):
            ranks[num]=i+1
        for i, num in enumerate(arr):
            arr[i]=ranks[num]
        return arr