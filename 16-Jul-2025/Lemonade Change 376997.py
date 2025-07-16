# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_freq = 0
        ten_freq = 0
        
        for bill in bills:
            if bill == 5:
                five_freq += 1
            elif bill == 10:
                if five_freq == 0:
                    return False
                five_freq -= 1
                ten_freq += 1
            elif bill == 20:
                if ten_freq > 0 and five_freq > 0:
                    ten_freq -= 1
                    five_freq -= 1
                elif five_freq >= 3:
                    five_freq -= 3
                else:
                    return False
        return True