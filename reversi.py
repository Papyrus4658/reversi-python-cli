import random
import time

import constants as c
import values as v


def select_turn() -> int:
    print(c.GREETING)

    while True:
        try:
            v.player_turn = int(input(c.PROMPT_SELECT_TURN + c.PROMPT_SYMBOL))

            if v.player_turn == c.BLACK or v.player_turn == c.WHITE:
                v.com_turn = v.player_turn * -1
                return
            else:
                print(c.INPUT_ERROR)
        except ValueError:
            print(c.INPUT_ERROR)


def set_board():
    # すべてのマスを空にする
    for y in range(1, c.ROWS + 1):
        for x in range(1, c.COLS + 1):
            v.board[y][x] = c.SPACE

    # 最初に配置する石
    v.board[c.ROWS / 2][c.COLS / 2] = v.board[c.ROWS / 2 + 1][c.COLS / 2 + 1] = c.WHITE
    v.board[c.ROWS / 2][c.COLS / 2 + 1] = v.board[c.ROWS / 2 + 1][c.COLS / 2] = c.BLACK


def play() -> None:
    turn_counts = 0
    current_turn = c.BLACK
    pass_count = 0

    print(c.GAME_START)

    for _ in range(c.ROWS * c.COLS):
        valid_squares = check_valid(current_turn)

        if len(valid_squares) > 0:
            pass_count = 0

            draw_board()

            count_stones()

            move = (
                player_move(valid_squares)
                if current_turn == v.player_turn
                else com_move(valid_squares)
            )

            reverse(move)

            turn_counts += 1
        else:
            pass_count += 1

            if pass_count > 1:
                break

            print(c.PASS)
            time.sleep(1)

        current_turn *= -1

    print(result())


def check_valid(current_turn) -> []:
    valid_squares = []

    for y in range(1, c.ROWS + 1):
        for x in range(1, c.COLS):
            if v.board[y][x] == c.SPACE:
                valid_squares.append(check_around(x, y, current_turn))
    return valid_squares


def check_around(x, y, current_turn) -> int[2]:
    aro_y = y
    aro_x = x
    opponent = current_turn * -1

    for coe_y in range(-1, 2):
        aro_y += coe_y

        for coe_x in range(-1, 2):
            aro_x += coe_x

            if v.board[aro_y][aro_x] == opponent:
                return check_front(aro_x, aro_y, coe_x, coe_y, current_turn, opponent)


def check_front(aro_x, aro_y, coe_x, coe_y, current_turn, opponent) -> int[2]:
    fro_y = aro_y
    fro_x = aro_x

    while v.board[fro_y][fro_x] == opponent:
        fro_y += coe_y
        fro_x += coe_x

        if v.board[fro_y][fro_x] == current_turn:
            return v.board[fro_y][fro_x]

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


def count_stones() -> int[2]:
    bc = wc = 0

    for y in range(1, c.ROWS + 1):
        for x in range(1, c.COLS + 1):
            if v.board[y][x] == c.BLACK:
                bc += 1
            elif v.board[y][x] == c.WHITE:
                wc += 1

    print("黒の数:", bc, "\t白の数:", wc)

    return [bc, wc]


def player_move(valid_squares) -> int[2]:
    return


def com_move(valid_squares) -> int[2]:
    print(c.COM_THINKING)
    time.sleep(2)

    return valid_squares[random.randint(0, len(valid_squares))]


def reverse(move):
    return


def result() -> str:
    print(c.GAME_OVER)

    final_counts = count_stones()

    print(c.BLACK_COUNT, final_counts[0], c.WHITE_COUNT, final_counts[1])

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
