class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr=[]
        num=1
        if n%2!=0:
            arr.append(0)
        while len(arr)<n:
            arr.append(num)
            arr.append(-num)
            num+=1
        return arr