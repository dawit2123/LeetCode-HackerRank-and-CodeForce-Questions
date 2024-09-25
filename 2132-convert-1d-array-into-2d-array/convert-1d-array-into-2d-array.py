class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        j=0
        two_dimensional_arr=[]
        if m*n != len(original):
            return []
        for i in range(m):
            two_dimensional_arr.append(original[j:j+n])
            j+=n
        return two_dimensional_arr