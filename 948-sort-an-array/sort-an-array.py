class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #base case for the recursive function
        if len(nums)<=1:
            return nums
        mid= len(nums)//2
        sorted_part1= self.sortArray(nums[:mid])
        sorted_part2= self.sortArray(nums[mid:])

        return self.merge(sorted_part1, sorted_part2) 
    def merge(self, sorted_part1, sorted_part2):
        res=[]
        i, j= 0,0
        while i<len(sorted_part1) and j<len(sorted_part2):
            if sorted_part1[i]<=sorted_part2[j]:
                res.append(sorted_part1[i])
                i+=1
            else:
                res.append(sorted_part2[j])
                j+=1
        res.extend(sorted_part1[i:])
        res.extend(sorted_part2[j:])
        return res               