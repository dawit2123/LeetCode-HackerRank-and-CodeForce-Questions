class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=0
        r=n
        is_left=True
        numbers=[]
        for i in range(0,len(nums)):
            if(is_left==True):
                numbers.append(nums[l])
                l+=1
                is_left=False
            else:
                numbers.append(nums[r])
                r+=1
                is_left=True
        return numbers
