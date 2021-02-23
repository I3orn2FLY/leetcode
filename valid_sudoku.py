def check_n(ch):
    return ord(ch) >= ord('1') and ord(ch) <= ord('9')


class Solution:
    def isValidSudoku(self, board) -> bool:

        for i in range(9):
            row_set = set()
            for j in range(9):
                ch = board[i][j]
                if ch == ".": continue
                if not check_n(ch): return False
                if ch in row_set: return False
                row_set.add(ch)

        for j in range(9):
            col_set = set()
            for i in range(9):
                ch = board[i][j]
                if ch == ".": continue
                if ch in col_set: return False
                col_set.add(ch)

        for i in range(3):
            for j in range(3):
                cell_set = set()
                for l in range(i * 3, (i + 1) * 3):
                    for m in range(j * 3, (j + 1) * 3):
                        ch = board[l][m]
                        if ch == ".": continue
                        if ch in cell_set: return False
                        cell_set.add(ch)

        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

s = Solution()
print(s.isValidSudoku(board))
