import constants as c

board = [
    [c.WALL if (x == 0 or x == 9 or y == 0 or y == 9) else 0 for x in range(c.COLS + 2)]
    for y in range(c.ROWS + 2)
]

player_turn = c.BLACK
com_turn = c.WHITE
