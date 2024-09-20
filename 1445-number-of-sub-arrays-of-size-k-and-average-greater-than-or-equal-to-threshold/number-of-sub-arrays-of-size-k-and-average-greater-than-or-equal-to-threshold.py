class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sub_arr=[]
        total_num=0
        for val in arr:
            if(len(sub_arr)==k-1):
                sub_arr.append(val)
                if (sum(sub_arr)/k)>=threshold:
                    total_num+=1
                sub_arr.remove(sub_arr[0])
            else:
                sub_arr.append(val)
        return total_num

