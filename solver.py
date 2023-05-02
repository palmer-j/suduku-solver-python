import collections
import logging

logging.basicConfig(level=logging.DEBUG)

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

    def is_valid(self):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = self.grid[r][c]
                if val == 0:
                    continue
                # check rows
                if val in rows[r]:
                    logging.debug(f'dupe {val} in row {r}')
                    return False
                else:
                    rows[r].add(val)
                # check cols
                if val in cols[c]:
                    logging.debug(f'dupe {val} in col {c}')
                    return False
                else:
                    cols[c].add(val)
                # check sqrs
                key = (r // 3) * 3 + c // 3
                if val in sqrs[key]:
                    logging.debug(f'dupe {val} in sqr {key}')
                    return False
                else:
                    sqrs[key].add(val)
        return True


if __name__ == '__main__':
    sb = SodukuBoard(test_grid)
    print(sb)
    print(sb.is_valid())