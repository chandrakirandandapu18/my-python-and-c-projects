board = [" " for i in range(9)]


def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(mark):
    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for w in wins:
        if board[w[0]] == mark and board[w[1]] == mark and board[w[2]] == mark:
            return True

    return False


def draw():
    return " " not in board


player = 1

while True:

    show_board()

    if player == 1:
        mark = "X"
    else:
        mark = "O"

    print("Player", player, "turn")

    pos = int(input("Choose position (1-9): ")) - 1

    if pos < 0 or pos > 8:
        print("Invalid position")
        continue

    if board[pos] != " ":
        print("Already occupied!")
        continue

    board[pos] = mark

    if winner(mark):
        show_board()
        print("Player", player, "wins 🎉")
        break

    if draw():
        show_board()
        print("Draw!")
        break

    if player == 1:
        player = 2
    else:
        player = 1

