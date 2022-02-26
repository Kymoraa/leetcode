"""
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  Y
ou may return any path that does so.

> Example 1:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"

> Example 2:
Input: target = "code"
Output: "RR!DDRR!UUL!R!"

N/B. I had to seek some guidance from the discussions to make this solution run. Implementing the edge case with 'z' was
not working as expected with my solution


"""


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = dict()
        for index, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
            row = index // 5
            col = index - 5 * row
            board[char] = (row, col)

        start_row, start_col = 0, 0
        output = ''
        prev_char = ''

        for letter in target:
            cur_row, cur_col = board[letter]
            row_diff = cur_row - start_row
            col_diff = cur_col - start_col

            if prev_char == 'z':
                if row_diff < 0:
                    output += 'U' * (-row_diff)
                elif row_diff > 0:
                    output += 'D' * row_diff
                if col_diff > 0:
                    output += 'R' * col_diff
                elif col_diff < 0:
                    output += 'L' * (-col_diff)
            else:
                if col_diff > 0:
                    output += 'R' * col_diff
                elif col_diff < 0:
                    output += 'L' * (-col_diff)
                if row_diff < 0:
                    output += 'U' * (-row_diff)
                elif row_diff > 0:
                    output += 'D' * row_diff

            prev_char = letter
            output += '!'
            start_row, start_col = cur_row, cur_col
        return output
