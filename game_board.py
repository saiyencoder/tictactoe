BOARD = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]


def board(position="", mark=""):
    # Mark X or O on board
    # if position != "" and mark != "":
    if position == 9:
        BOARD[0][2] = mark
    elif position == 8:
        BOARD[0][1] = mark
    elif position == 7:
        BOARD[0][0] = mark
    elif position == 6:
        BOARD[1][2] = mark
    elif position == 5:
        BOARD[1][1] = mark
    elif position == 4:
        BOARD[1][0] = mark
    elif position == 3:
        BOARD[2][2] = mark
    elif position == 2:
        BOARD[2][1] = mark
    elif position == 1:
        BOARD[2][0] = mark

    # Print Board
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)
    print(f"  {BOARD[0][0]}  |  {BOARD[0][1]}  |  {BOARD[0][2]}  ")
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)
    print("-" * 18)
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)
    print(f"  {BOARD[1][0]}  |  {BOARD[1][1]}  |  {BOARD[1][2]}  ")
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)
    print("-" * 18)
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)
    print(f"  {BOARD[2][0]}  |  {BOARD[2][1]}  |  {BOARD[2][2]}  ")
    print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)

    # Check if there is a 3 in a row
    if (BOARD[0][0] == BOARD[0][1] == BOARD[0][2] == mark) or \
       (BOARD[1][0] == BOARD[1][1] == BOARD[1][2] == mark) or \
       (BOARD[2][0] == BOARD[2][1] == BOARD[2][2] == mark) or \
       (BOARD[0][0] == BOARD[1][0] == BOARD[2][0] == mark) or \
       (BOARD[0][1] == BOARD[1][1] == BOARD[2][1] == mark) or \
       (BOARD[0][2] == BOARD[1][2] == BOARD[2][2] == mark) or \
       (BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == mark) or \
       (BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == mark):
        print(f'\n{mark} wins!')
        return True
