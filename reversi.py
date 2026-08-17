import constants as c
import values as v


def select_turn() -> int:
    print("先手/後手を決定します。")

    while True:
        try:
            player = int(
                input(
                    "先手なら", c.BLACK, "、後手なら", c.WHITE, "を入力してください。"
                )
            )

            if player == c.BLACK or player == c.WHITE:
                return player
            else:
                print("正しい値を入力してください。")
        except ValueError:
            print("数値を入力してください。")


def set_board():
    # すべてのマスを空にする
    for y in range(1, c.ROWS + 1):
        for x in range(1, c.COLS + 1):
            v.board[y][x] = c.SPACE

    # 最初に配置する石
    v.board[c.ROWS / 2][c.COLS / 2] = v.board[c.ROWS / 2 + 1][c.COLS / 2 + 1] = c.WHITE
    v.board[c.ROWS / 2][c.COLS / 2 + 1] = v.board[c.ROWS / 2 + 1][c.COLS / 2] = c.BLACK


def play():
    return


def check_valid():
    return


def check_around():
    return


def check_front():
    return


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


def player_move():
    return


def com_move():
    return


def reverse():
    return


def result() -> str:
    final_count = count_stones()

    print(c.BLACK_COUNT, final_count[0], c.WHITE_COUNT, final_count[1])

    if final_count[0] > final_count[1]:
        return c.BLACK_WIN
    elif final_count[0] < final_count[1]:
        return c.WHITE_WIN
    else:
        return c.DRAW


def main():
    print(c.GREETING)

    # 先後の決定
    v.player_turn = select_turn()
    v.com_turn = v.player_turn * -1

    # 盤をリセット
    set_board()

    # 対局

    # 終局
    print(result)


if __name__ == "__main__":
    main()
