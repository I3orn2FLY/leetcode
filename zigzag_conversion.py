class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        row = 0
        down = True

        row2str = ['' for _ in range(numRows)]
        for i in range(len(s)):
            if row == numRows:
                down = not down
                row = numRows - 2
            elif row == -1:
                down = not down
                row = 1

            row2str[row] += s[i]
            if down:
                row += 1
            else:
                row -= 1

        return ''.join(row2str)


print(Solution().convert("PAYPALISHIRING", 4))
