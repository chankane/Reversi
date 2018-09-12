import numpy as np
import string


BLACK = 0
WHITE = 1
# do not change it
BOARD_SIZE = 8


def init():
    if BLACK:
        return np.array([0x0000001008000000, 0x0000000810000000], dtype=np.uint64)
    else:
        # return np.array([0x0000000000000000, 0x0000000000000000], dtype=np.uint64)
        return np.array([0x0000000810000000, 0x0000001008000000], dtype=np.uint64)


def move(stones, pos, turn):
    digit = to_digit(pos)
    if not 0 <= digit < BOARD_SIZE * BOARD_SIZE:
        return False
    stones[turn] |= np.uint64(1) << np.uint64(digit)
    return True


def to_digit(pos):
    if len(pos) is not 2 or not pos[0].isalpha() or not pos[1].isdecimal():
        return -1
    pos = pos.upper()
    x = string.ascii_uppercase.index('H') - string.ascii_uppercase.index(pos[0])
    y = 8 - int(pos[1])
    return y * BOARD_SIZE + x


def is_finished(stones):
    return 0xFFFFFFFFFFFFFFFF == stones[BLACK] | stones[WHITE]


def display(stones):
    print("  A B C D E F G H")
    for i in range(BOARD_SIZE * BOARD_SIZE):
        if not i % 8:
            print(i // 8 + 1, end=" ")
        shift_num = BOARD_SIZE * BOARD_SIZE - 1 - i
        if stones[BLACK] >> np.uint64(shift_num) & np.uint64(1):
            # 'end=""' means no "\n"
            print("*", end=" ")
        elif stones[WHITE] >> np.uint64(shift_num) & np.uint64(1):
            print("O", end=" ")
        else:
            print(".", end=" ")
        if not shift_num % 8:
            print()


def main():
    stones = init()
    display(stones)
    while not is_finished(stones):
        if not move(stones, input(), 0):
            print("Invalid move...")
            continue
        display(stones)


if __name__ == "__main__":
    main()
