import board
import constants as c


class Game:
    def __init__(self, chose_stone, com_level):
        self.b = board.Board()
        self.player_turn = chose_stone if chose_stone == 1 else -1
        self.com_turn = self.player_turn * -1
        self.com_level = com_level
        self.current_turn = 1

    def play_game(self) -> str:
        pass_count = 0

        while pass_count < 2:
            valid_squares = self.check_squares()

            if len(valid_squares) > 0:
                self.draw_board()

                self.reverse_stones(
                    self.player_move(valid_squares)
                    if self.current_turn == self.player_turn
                    else self.com_move1(valid_squares)
                )

                pass_count = 0
            else:
                pass_count += 1

            self.current_turn *= -1

        return self.end_game()

    def check_squares(self) -> list:
        valid_squares = []

        for y in range(1, c.COLS + 1):
            for x in range(1, c.ROWS + 1):
                if self.b.b[y][x] == c.BS.get("SPACE"):
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            next_y = y + i
                            next_x = x + j

                            if self.b.b[next_y][next_x] == self.current_turn * -1:
                                while True:
                                    next_y += i
                                    next_x += j

                                    if self.b.b[next_y][next_x] == self.current_turn:
                                        valid_squares.append([y, x])
                                        break
                                    elif self.b.b[next_y][next_x] == c.BS.get("SPACE"):
                                        break
                                    elif self.b.b[next_y][next_x] == c.BS.get("WALL"):
                                        break
                                    elif (
                                        self.b.b[next_y][next_x]
                                        == self.current_turn * -1
                                    ):
                                        continue

        return valid_squares

    def draw_board(self):
        print("　　１　２　３　４　５　６　７　８")
        print("　＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋")

        for y in range(c.COLS):
            print(" " + str(y + 1), end="")

            for x in range(c.ROWS):
                status = (
                    "⚫️"
                    if self.b.b[y + 1][x + 1] == 1
                    else "⚪️"
                    if self.b.b[y + 1][x + 1] == -1
                    else "　"
                )

                print("｜" + status, end="")

            print("｜")
            print("　＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋ー＋")

    def player_move(self, valid_squares) -> list:
        is_thinking = True
        print("あなたの番です。")
        print("打つマスを選択します。")

        while is_thinking:
            coord = []

            for i in c.AXES:
                coord.append(self.input_coord(i))

            for i in valid_squares:
                if coord == i:
                    is_thinking = False

            if is_thinking:
                print("そこには打てません")

        return coord

    def input_coord(self, axis) -> int:
        while True:
            try:
                coord = int(input(axis + ">"))

                if coord >= 1 and coord <= 8:
                    print(coord)
                    return coord
                else:
                    print("無効な値です。1~8の範囲で入力してください。")
            except ValueError:
                print("無効な値です。1~8の範囲で入力してください。")

        return coord

    def reverse_stones(self, coord):
        y = coord[0]
        x = coord[1]

        self.b.b[y][x] = self.current_turn

        for i in range(-1, 2):
            for j in range(-1, 2):
                next_y = y + i
                next_x = x + j

                if self.b.b[next_y][next_x] == self.current_turn * -1:
                    scan_y = next_y
                    scan_x = next_x

                    while self.b.b[scan_y][scan_x] == self.current_turn * -1:
                        scan_y += i
                        scan_x += j

                        if self.b.b[scan_y][scan_x] == self.current_turn:
                            flip_y = next_y
                            flip_x = next_x

                            while flip_y != scan_y or flip_x != scan_x:
                                self.b.b[flip_y][flip_x] = self.current_turn
                                flip_y += i
                                flip_x += j

                            break
                        elif self.b.b[next_y][next_x] == c.BS.get("SPACE"):
                            break
                        elif self.b.b[next_y][next_x] == c.BS.get("WALL"):
                            break
                        elif self.b.b[next_y][next_x] == self.current_turn * -1:
                            continue

    def end_game(self) -> str:
        print("対局が終了しました。")
        self.draw_board()
        stones = self.count_stones()

        if stones[0] > stones[1]:
            if self.player_turn == c.BS.get("BLACK"):
                return c.RESULTS.get("WIN")
            else:
                return c.RESULTS.get("LOSE")
        elif stones[0] < stones[1]:
            if self.player_turn == c.BS.get("BLACK"):
                return c.RESULTS.get("LOSE")
            else:
                return c.RESULTS.get("WIN")
        else:
            return c.RESULTS.get("DRAW")

    def count_stones(self) -> list:
        bc = wc = 0

        for y in range(1, c.COLS + 1):
            for x in range(1, c.ROWS + 1):
                if self.b.b[y][x] == c.BS.get("BLACK"):
                    bc += 1
                elif self.b.b[y][x] == c.BS.get("WHITE"):
                    wc += 1

        print("黒：", bc)
        print("白：", wc)
        return [bc, wc]
