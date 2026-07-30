import random

player1 = 0
player2 = 0

snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 5
}

ladders = {
    3: 22,
    8: 26,
    28: 76,
    58: 77
}

def roll_dice():
    return random.randint(1,6)

while True:
    input("\nPlayer 1 turn - Press Enter to roll dice")
    dice = roll_dice()
    print("Player 1 rolled:", dice)

    if player1 + dice <= 100:
        player1 += dice

    if player1 in ladders:
        print("🪜 Ladder! You climbed up!")
        player1 = ladders[player1]

    elif player1 in snakes:
        print("🐍 Snake! You went down!")
        player1 = snakes[player1]

    print("Player 1 position:", player1)

    if player1 == 100:
        print("🎉 Player 1 wins!")
        break


    input("\nPlayer 2 turn - Press Enter to roll dice")
    dice = roll_dice()
    print("Player 2 rolled:", dice)

    if player2 + dice <= 100:
        player2 += dice

    if player2 in ladders:
        print("🪜 Ladder! You climbed up!")
        player2 = ladders[player2]

    elif player2 in snakes:
        print("🐍 Snake! You went down!")
        player2 = snakes[player2]

    print("Player 2 position:", player2)

    if player2 == 100:
        print("🎉 Player 2 wins!")
        break