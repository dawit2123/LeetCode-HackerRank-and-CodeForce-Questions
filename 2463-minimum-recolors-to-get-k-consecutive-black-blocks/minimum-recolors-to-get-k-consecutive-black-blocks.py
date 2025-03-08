class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        recolor=k
        white=0
        for right in range(len(blocks)):
            if blocks[right]=="W":
                white+=1
            if right-left+1==k:
                recolor= min(recolor, white)
                if blocks[left]=="W":
                    white-=1
                left+=1
        return recolor