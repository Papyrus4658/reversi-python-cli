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
    for y in range(1, 9):
        for x in range(1, 9):
            v.board[y][x] = 0

    # 最初に配置する石
    v.board[4][4] = v.board[5][5] = c.WHITE
    v.board[4][5] = v.board[5][4] = c.BLACK


def count_stones() -> int[2]:
    bc = wc = 0

    for y in range(1, 9):
        for x in range(1, 9):
            if v.board[y][x] == 1:
                bc += 1
            elif v.board[y][x] == -1:
                wc += 1

    print("黒の数:", bc, "\t白の数:", wc)

    return [bc, wc]


def main():
    print("ようこそ！")
    print("ここではリバーシをプレイできます。")

    # 先後の決定
    player = select_turn()
    com = player * -1

    # 盤をリセット
    set_board()

    # 対局

    # 終局

    return


if __name__ == "__main__":
    main()
