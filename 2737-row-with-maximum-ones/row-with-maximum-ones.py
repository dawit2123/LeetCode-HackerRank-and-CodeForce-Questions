class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index, maximum= 0, 0
        for i in range(len(mat)):
            count=0
            for val in mat[i]:
                if val==1:
                    count+=1
            if count>maximum:
                maximum=count
                index=i
        return [index, maximum]