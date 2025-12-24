class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple_sum=sum(apple)
        capacity.sort()
        result_sum=0
        count=0
        for i in range(len(capacity)-1, -1, -1):
            if result_sum<apple_sum:
                count+=1
                result_sum+=capacity[i]
            else:
                break
        return count