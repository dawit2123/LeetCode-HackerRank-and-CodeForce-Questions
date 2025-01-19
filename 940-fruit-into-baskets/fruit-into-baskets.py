class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maximum_number_of_fruits=0
        count=defaultdict(int)
        left, res, total= 0,0,0
        for right in range(len(fruits)):
            count[fruits[right]]+=1
            while len(count)>2:
                total-=1
                count[fruits[left]]-=1
                if count[fruits[left]]==0:
                    count.pop(fruits[left])
                left+=1
            total+=1
            res=max(res, total)
        return res
