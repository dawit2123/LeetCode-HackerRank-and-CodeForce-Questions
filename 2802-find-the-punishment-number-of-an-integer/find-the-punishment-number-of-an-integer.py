class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishment_numbers_sum=0
        def partition(i, cur, target, string):
            if i==len(string) and cur==target:
                return True
            # partition
            for j in range(i, len(string)):
                if partition(j+1, cur+int(string[i:j+1]), target, string):
                    return True
            
        for i in range(1, n+1):
            if partition(0, 0, i, str(i**2)):
                punishment_numbers_sum+=i**2            
        return punishment_numbers_sum

