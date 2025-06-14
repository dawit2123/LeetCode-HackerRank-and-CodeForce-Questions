class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = str(num)
        max_num = str_num
        for digit in str_num:
            if digit != '9':
                max_num = str_num.replace(digit, '9')
                break
        min_num = str_num
        for digit in str_num:
            if digit != '0':
                min_num = str_num.replace(digit, '0')
                break
        
        return int(max_num) - int(min_num)