class Solution:
    def minSwaps(self, s: str) -> int:
        max_closing, closing= 0, 0
        for c in s:
            if c=="[":
                closing-=1
            else:
                closing+=1
                max_closing=max(closing, max_closing)
        return (max_closing+1)//2

        