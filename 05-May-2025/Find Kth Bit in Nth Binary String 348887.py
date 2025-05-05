# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length= 2**n -1
        invert=False
        while length>1:
            half=length//2
            if k<=half:
                length=half
            elif k> half+1:
                k= 1+length-k
                length= half
                invert= not invert
            else:
                return "1" if not invert else "0"
        return "0" if not invert else "1"
