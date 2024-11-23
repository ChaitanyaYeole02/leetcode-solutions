class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box), len(box[0])
        result = [["."] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            i = COLS - 1

            for c in reversed(range(COLS)):
                if box[r][c] == '#':
                    result[i][ROWS - r - 1] = '#'
                    i -= 1
                elif box[r][c] == '*':
                    result[c][ROWS -r - 1] = '*'
                    i = c - 1

        return result
