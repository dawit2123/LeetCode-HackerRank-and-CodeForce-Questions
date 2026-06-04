class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count={}
        for num in nums:
            nums_count[num]=nums_count.get(num, 0)+1
        bucket=[[] for i in range(len(nums)+1)]
        for num in nums_count.keys():
            freq=nums_count[num]
            bucket[freq].append(num)
        result=[]
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result