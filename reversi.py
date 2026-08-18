import inspect
import random
import time

import constants as c
import values as v


def select_turn() -> None:
    print(c.SELECT_TURN_CALLED)

    while True:
        try:
            print("先手なら", c.BLACK, "、後手なら", c.WHITE, "を入力> ", end="")
            v.player_turn = int(input())

            if v.player_turn == c.BLACK or v.player_turn == c.WHITE:
                v.com_turn = v.player_turn * -1
                return
            else:
                print(c.INPUT_ERROR)
        except ValueError:
            print(c.INPUT_ERROR)


def set_board() -> None:
    # すべてのマスを空にする
    for y in range(1, c.ROWS + 1):
        for x in range(1, c.COLS + 1):
            v.board[y][x] = c.SPACE

    # 最初に配置する石
    row_center = int(c.ROWS / 2)
    col_center = int(c.COLS / 2)

    v.board[row_center][col_center] = c.WHITE
    v.board[row_center + 1][col_center + 1] = c.WHITE
    v.board[row_center][col_center + 1] = c.BLACK
    v.board[row_center + 1][col_center] = c.BLACK


def play() -> None:
    current_turn = 0
    cur = c.BLACK
    pass_count = 0

    print(c.GAME_START)

    for _ in range(c.ROWS * c.COLS - 4):
        draw_board()
        valid_squares = check_valid(cur)

        if len(valid_squares) > 0:
            current_turn += 1
            print(current_turn, "手目")
            pass_count = 0

            count_stones()

            print(valid_squares)

            move = (
                player_move(valid_squares)
                if cur == v.player_turn
                else com_move(valid_squares)
            )

            if move == [-1, -1]:
                print(c.SURRENDER)
                return

            check_around(move[0], move[1], cur)
        else:
            pass_count += 1

            if pass_count > 1:
                break

            print(c.PASS)
            time.sleep(1)

        cur *= -1

    print(result())


def check_valid(cur) -> list:
    valid_squares = []

    for y in range(1, c.ROWS + 1):
        for x in range(1, c.COLS + 1):
            front = check_around(y, x, cur)

            if v.board[y][x] == c.SPACE and front is not None:
                valid_squares.append([y, x])

    return valid_squares


def check_around(y, x, cur) -> list:
    aroy = y
    arox = x

    for coey in range(-1, 2):
        aroy = y + coey

        for coex in range(-1, 2):
            if coey != 0 or coex != 0:
                arox = x + coex

                if v.board[aroy][arox] == cur * -1:
                    front = check_front(aroy, arox, coey, coex, cur)

                    caller = inspect.stack()[1].function

                    if front is not None:
                        if caller == "check_valid":
                            return front
                        else:
                            froy = front[0]
                            frox = front[1]

                            reverse(froy, frox, coey, coex, cur)
                            v.board[y][x] = cur


def check_front(aroy, arox, coey, coex, cur) -> list:
    froy = aroy
    frox = arox

    while v.board[froy][frox] == cur * -1:
        froy += coey
        frox += coex

        if v.board[froy][frox] == cur:
            return [froy, frox]


def draw_board() -> None:
    print(" ")
    for x in range(1, c.COLS + 1):
        print(" ", x, end="")

    draw_line()

    for y in range(1, c.ROWS + 1):
        print(y, end="|")

        for x in range(1, c.COLS + 1):
            if v.board[y][x] == c.BLACK:
                print("⚫", end="|")
            elif v.board[y][x] == c.WHITE:
                print("⚪", end="|")
            else:
                print("　", end="|")

        draw_line()


def draw_line() -> None:
    print()
    print(" ", end="")

    for _ in range(c.COLS):
        print("+ー", end="")

    print("+")


def count_stones() -> list:
    bc = wc = 0

    for y in range(1, c.ROWS + 1):
        for x in range(1, c.COLS + 1):
            if v.board[y][x] == c.BLACK:
                bc += 1
            elif v.board[y][x] == c.WHITE:
                wc += 1

    print(c.BC, bc, " ", c.WC, wc)

    return [bc, wc]


def player_move(valid_squares) -> list:
    print(c.PLAYER_MOVE_CALLED)

    while True:
        try:
            y = int(input(c.PROMPT_Y))
            x = int(input(c.PROMPT_X))
            move = [y, x]

            for s in valid_squares:
                if move == s or move == [-1, -1]:
                    return move

            print(c.INPUT_ERROR)
        except ValueError:
            print(c.INPUT_ERROR)


def com_move(valid_squares) -> list:
    print(c.COM_THINKING)
    time.sleep(2)

    return valid_squares[random.randint(0, len(valid_squares) - 1)]


def reverse(y, x, coey, coex, cur) -> None:
    while v.board[y][x] == cur:
        y -= coey
        x -= coex

        v.board[y][x] *= -1


def result() -> str:
    print(c.GAME_OVER)
    draw_board()
    final_counts = count_stones()

    if final_counts[0] > final_counts[1]:
        return c.BLACK_WIN
    elif final_counts[0] < final_counts[1]:
        return c.WHITE_WIN
    else:
        return c.DRAW


def main() -> None:
    print(c.GREETING)

    select_turn()

    set_board()

    play()


if __name__ == "__main__":
    main()
