class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result=0
        current_index=0
        while current_index<len(neededTime):
            group_start=current_index
            group_sum=0
            max_value=0
            while current_index<len(neededTime) and colors[group_start]==colors[current_index]:
                cur_time=neededTime[current_index]
                group_sum+=(cur_time)
                if cur_time>max_value:
                    max_value=cur_time
                current_index+=1
            if current_index-group_start>1:
                result+=(group_sum-max_value)
        return result

                