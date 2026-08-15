import time
import random


class ComLevel1:
    def com_move1(self, valid_squares) -> list:
        print("COMの番です。")
        time.sleep(1)
        coord = random.choice(valid_squares)
        return coord
