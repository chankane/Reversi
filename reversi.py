import numpy as np


BLACK = 0
WHITE = 1
# do not change it
BOARD_SIZE = 8


def init():
    if BLACK:
        return np.array([0x0000001008000000, 0x0000000810000000])
    else:
        return np.array([0x0000000810000000, 0x0000001008000000])


def put(stones, pos, turn):
    digit = to_digit(pos)
    if not 0 < digit <= BOARD_SIZE * BOARD_SIZE:
        return False
    stones[turn] |= 1 << digit


def to_digit(pos):
    pos = pos.upper()
    x = int(pos[0]) - int('A')
    y = int(pos[1]) - 1
    return y * BOARD_SIZE + x


def is_finished(stones):
    return 0xFFFFFFFFFFFFFFFF == stones[BLACK] | stones[WHITE]


def display(stones):
    for i in range(BOARD_SIZE * BOARD_SIZE):
        shift_num = BOARD_SIZE * BOARD_SIZE - 1 - i
        if stones[BLACK] >> shift_num & 1:
            # 'end=""' means no "\n"
            print("#", end="")
        elif stones[WHITE] >> shift_num & 1:
            print("O", end="")
        else:
            print(".", end="")
        if not shift_num % 8:
            print()


def main():
    stones = init()
    display(stones)
    while not is_finished(stones):
        put(stones, input(), 0)
        display(stones)


if __name__ == "__main__":
    main()
