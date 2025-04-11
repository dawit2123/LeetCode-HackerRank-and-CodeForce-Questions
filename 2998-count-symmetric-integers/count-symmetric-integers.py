class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        number_of_symmetric=0
        for num in range(low, high+1):
            num_string= str(num)
            length_of_num_string=len(num_string)
            if length_of_num_string%2==0:
                print(num_string)
                if sum([int(val) for val in num_string[:length_of_num_string//2]])==sum([int(val) for val in num_string[length_of_num_string//2:]]):
                    number_of_symmetric+=1
        return number_of_symmetric