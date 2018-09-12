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
        # return np.array([0xFFFFFFFFFFFFFFFF, 0x0000000000000000], dtype=np.uint64)
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
    print("\n  A B C D E F G H")
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
            print("")


def show_result(stones):
    b = count1(stones[BLACK])
    w = count1(stones[WHITE])
    print("\n-------- Game over --------")
    print("Black: " + str(b))
    print("White: " + str(w))
    if b > w:
        print("Black won")
    elif b < w:
        print("White won")
    else:
        print("Draw game")


def count1(stone):
    stone = (stone & np.uint64(0x5555555555555555)) + (stone >> np.uint64(1) & np.uint64(0x5555555555555555))
    stone = (stone & np.uint64(0x3333333333333333)) + (stone >> np.uint64(2) & np.uint64(0x3333333333333333))
    stone = (stone & np.uint64(0x0F0F0F0F0F0F0F0F)) + (stone >> np.uint64(4) & np.uint64(0x0F0F0F0F0F0F0F0F))
    stone = (stone & np.uint64(0x00FF00FF00FF00FF)) + (stone >> np.uint64(8) & np.uint64(0x00FF00FF00FF00FF))
    stone = (stone & np.uint64(0x0000FFFF0000FFFF)) + (stone >> np.uint64(16) & np.uint64(0x0000FFFF0000FFFF))
    return (stone & np.uint64(0x00000000FFFFFFFF)) + (stone >> np.uint64(32) & np.uint64(0x00000000FFFFFFFF))


def main():
    stones = init()
    display(stones)
    while not is_finished(stones):
        if not move(stones, input(), 0):
            print("Invalid move...")
            continue
        display(stones)
    show_result(stones)


if __name__ == "__main__":
    main()
