# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        num_bits= bin(num)[2:]
        bits=""
        for bit in num_bits:
            bits+=("1" if bit=="0" else "0")
        return int(bits, 2)