from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict=defaultdict(set)
        col_dict=defaultdict(set)
        sub_box_dict=defaultdict(set)
        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num==".":
                    continue
                else:
                    if (num in row_dict[r]) or (num in col_dict[c]) or (num in sub_box_dict[(r//3, c//3)]):
                        return False
                    else:
                        row_dict[r].add(num)
                        col_dict[c].add(num)
                        sub_box_dict[(r//3, c//3)].add(num)
        return True