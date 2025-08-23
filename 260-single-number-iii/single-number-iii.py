class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_set_numbers= reduce(xor, nums)
        pviot_bit= xor_set_numbers & -(xor_set_numbers)
        unique_number1= 0
        for num in nums:
            if num&pviot_bit:
                unique_number1^=num
        unique_number2= xor_set_numbers^unique_number1
        return [unique_number1, unique_number2]