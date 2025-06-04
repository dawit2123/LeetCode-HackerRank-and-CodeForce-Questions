# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL= len(board), len(board[0])
        path= set()
        # doing a recursive approach of using a depth first search
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or 
                c<0 or 
                r>=ROW or 
                c>=COL or 
                word[i]!=board[r][c] or 
                (r,c) in path):
                return False
            path.add((r,c))
            res= (dfs(r+1, c, i+1) or 
                dfs(r-1, c, i+1) or 
                dfs(r, c+1, i+1) or 
                dfs(r,c-1 , i+1))
            path.remove((r,c))
            return res
        for R in range(ROW):
            for C in range(COL):
                if dfs(R,C,0):
                    return True
        return False
