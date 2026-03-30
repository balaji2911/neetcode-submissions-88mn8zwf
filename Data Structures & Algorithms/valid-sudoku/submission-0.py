from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        subgrid_map = defaultdict(set)

        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_map[i] or board[i][j] in col_map[j]:
                    return False 
                i_subgrid = i//3
                j_subgrid = j//3
                if board[i][j] in subgrid_map[i_subgrid,j_subgrid]:
                    return False
                row_map[i].add(board[i][j])
                col_map[j].add(board[i][j])
                subgrid_map[i_subgrid,j_subgrid].add(board[i][j])
            
            # print("Row Map: ", row_map)
            # print("Col Map: ", col_map)
            # print("Subgrid Map: ", subgrid_map)

        return True