# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col= len(board), len(board[0])
        """
        Do not return anything, modify board in-place instead.
        """
        def capture(r, c):
            if min(r,c)<0 or r==row or c==col or board[r][c]!="O":
                return
            board[r][c]="T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c-1)
            capture(r, c+1)
        for r in range(row):
            for c in range(col):
                if board[r][c]=="O" and (r in [0, row-1] or c in [0, col-1]):
                    capture(r,c)
        # replacing "0" with "X"
        for r in range(row):
            for c in range(col):
                if board[r][c]=="O":
                    board[r][c]="X"
        
        # replacing "T" with "X"
        for r in range(row):
            for c in range(col):
                if board[r][c]=="T":
                    board[r][c]="O"
        return board