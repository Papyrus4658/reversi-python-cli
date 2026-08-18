import inspect
import random
import time

import constants as c
import values as v


def select_turn() -> None:
    print(c.GREETING)

    while True:
        try:
            v.player_turn = int(input(c.PROMPT_SELECT_TURN))

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
    v.board[c.ROWS / 2][c.COLS / 2] = c.WHITE
    v.board[c.ROWS / 2 + 1][c.COLS / 2 + 1] = c.WHITE
    v.board[c.ROWS / 2][c.COLS / 2 + 1] = c.BLACK
    v.board[c.ROWS / 2 + 1][c.COLS / 2] = c.BLACK


def play() -> None:
    turn_counts = 0
    cur = c.BLACK
    pass_count = 0

    print(c.GAME_START)

    for _ in range(c.ROWS * c.COLS):
        valid_squares = check_valid(cur)

        if len(valid_squares) > 0:
            pass_count = 0

            draw_board()

            count_stones()

            move = (
                player_move(valid_squares)
                if cur == v.player_turn
                else com_move(valid_squares)
            )

            if move == [-1, -1]:
                print(c.SURRENDER)
                return

            check_around(move[0], move[1])

            turn_counts += 1
        else:
            pass_count += 1

            if pass_count > 1:
                break

            print(c.PASS)
            time.sleep(1)

        cur *= -1

    print(result())


def check_valid(cur):
    valid_squares = []

    for y in range(1, c.ROWS + 1):
        for x in range(1, c.COLS):
            front = check_around(y, x, cur)

            if v.board[y][x] == c.SPACE and front is not None:
                valid_squares.append(v.board[y][x])

    print(type(valid_squares))
    return valid_squares


def check_around(y, x, cur):
    aroy = y
    arox = x

    for coey in range(-1, 2):
        aroy += coey

        for coex in range(-1, 2):
            arox += coex

            if v.board[aroy][arox] == cur * -1:
                front = check_front(aroy, arox, coey, coex, cur)

                caller = inspect.stack()[1].function

                if caller == "check_valid":
                    print(type(front))
                    return front
                else:
                    froy = front[0]
                    frox = front[1]

                    reverse(froy, frox, coey, coex, cur)


def check_front(aroy, arox, coey, coex, cur):
    froy = aroy
    frox = arox

    while v.board[froy][frox] == cur * -1:
        froy += coey
        frox += coex

        if v.board[froy][frox] == cur:
            return [froy, frox]

    return


def draw_board() -> None:
    print(" ")
    for x in range(1, c.COLS + 1):
        print(" " * 2, x, end="")

    draw_line()

    for y in range(1, c.ROWS + 1):
        print(y, end="|")

        for x in range(1, c.COLS):
            if v.board[y][x] == c.BLACK:
                print("●", end="|")
            elif v.board[y][x] == c.WHITE:
                print("◯", end="|")
            else:
                print("　", end="|")

        print()

        draw_line()


def draw_line() -> None:
    for _ in range(c.COLS):
        print("+ー", end="")

    print("+")


def count_stones():
    bc = wc = 0

    for y in range(1, c.ROWS + 1):
        for x in range(1, c.COLS + 1):
            if v.board[y][x] == c.BLACK:
                bc += 1
            elif v.board[y][x] == c.WHITE:
                wc += 1

    print(c.BC, bc, " ", c.WC, wc)

    print(type([bc, wc]))
    return [bc, wc]


def player_move(valid_squares):
    print(c.PLAYER_MOVE_CALLED)

    while True:
        try:
            y = int(input(c.PROMPT_Y))
            x = int(input(c.PROMPT_X))
            move = [y, x]

            return move
        except ValueError:
            print(c.INPUT_ERROR)


def com_move(valid_squares):
    print(c.COM_THINKING)
    time.sleep(2)

    return valid_squares[random.randint(0, len(valid_squares))]


def reverse(y, x, coey, coex, cur) -> None:
    while v.board[y][x] == cur:
        y -= coey
        x -= coex

        v.board[y][x] *= -1


def result() -> str:
    print(c.GAME_OVER)

    final_counts = count_stones()

    print(c.BC, final_counts[0], c.WC, final_counts[1])

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
