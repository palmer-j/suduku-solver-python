test_grid = [[5, 0, 0, 0, 8, 0, 0, 4, 9],
             [0, 0, 0, 5, 0, 0, 0, 3, 0],
             [0, 6, 7, 3, 0, 0, 0, 0, 1],
             [1, 5, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 2, 0, 8, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 8],
             [7, 0, 0, 0, 0, 4, 1, 5, 0],
             [0, 3, 0, 0, 0, 2, 0, 0, 0],
             [4, 9, 0, 0, 5, 0, 0, 0, 3]]


class SodukuBoard:
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        board_string = '╔═══════╦═══════╦═══════╗\n'
        for r in range(9):
            if r in [3, 6]:
                board_string += '╠═══════╬═══════╬═══════╣\n'
            board_string += '║ '
            for c in range(9):
                if c in [3, 6]:
                    board_string += '║ '
                if self.grid[r][c] == 0:
                    board_string += '. '
                else:
                    board_string += str(self.grid[r][c]) + ' '
            board_string += '║'
            board_string += '\n'
        board_string += '╚═══════╩═══════╩═══════╝'
        return board_string


if __name__ == '__main__':
    sb = SodukuBoard(test_grid)
    print(sb)
