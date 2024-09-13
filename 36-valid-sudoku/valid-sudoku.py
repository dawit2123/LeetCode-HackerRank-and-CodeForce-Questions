class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= defaultdict(set)
        cols= defaultdict(set)
        sub_board= defaultdict(set)
        for r in range(0,9):
            for c in range(0,9):
                if board[r][c]==".":
                    continue
                elif (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sub_board[(r//3, c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    sub_board[(r//3,c//3)].add(board[r][c])
        return True

        