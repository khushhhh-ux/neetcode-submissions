class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            seen = set()

            for num in row:
                if num == ".":
                    continue
                elif num in seen:
                    return False
                seen.add(num)

        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]

                if num == ".":
                    continue
                elif num in seen:
                    return False

                seen.add(num)

        for boxrow in range(0, 9, 3):
            for boxcol in range(0, 9, 3):
                seen = set()

                for row in range(boxrow, boxrow + 3):
                    for col in range(boxcol, boxcol + 3):
                        num = board[row][col]

                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)

        return True