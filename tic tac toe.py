board = [" " for i in range(9)]

def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_win(player):
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

    for combo in wins:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True

    return False


def check_draw():
    for i in board:
        if i == " ":
            return False
    return True


player = "X"

while True:
    display()

    position = int(input("Player " + player + " enter position (1-9): ")) - 1

    if position < 0 or position > 8:
        print("Invalid position")
        continue

    if board[position] != " ":
        print("Position already taken")
        continue

    board[position] = player

    if check_win(player):
        display()
        print("Player", player, "wins!")
        break

    if check_draw():
        display()
        print("Match Draw!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"