class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        unique_sets=set()
        prev=0
        for i in range(len(arr)):
            prev|=arr[i]
            current=0
            for j in range(i, -1, -1):
                current|=arr[j]
                unique_sets.add(current)
                if current==prev:
                    break
        return len(unique_sets)