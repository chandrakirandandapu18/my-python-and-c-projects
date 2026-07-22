import random

player_1 = input("Enter player 1 name : ")
player_2 = input("Enter player 2 name : ")

ladders = {
    8:12,
    17:26,
    29:35,
    43:56,
    65:71,
    79:87
}

snakes = {
    14:6,
    23:4,
    47:18,
    61:46,
    73:59,
    89:72,
    96:82
}

while True:

    player1 = 0
    player2 = 0

    print("========================================")
    print("\tSnake and Ladder")
    print("========================================")

    while True:

        # Player 1 turn
        input(f"\nPress Enter To Roll The Dice {player_1} ---->")

        dice = random.randint(1,6)
        print("You have rolled:", dice)

        if player1 + dice <= 100:
            player1 += dice
        else:
            print("You need exact number to win")

        if player1 in ladders:
            print("Hurrayyy.. You found a ladder |=|")
            player1 = ladders[player1]

        elif player1 in snakes:
            print("Oops you got bit by a snake... ~~~")
            player1 = snakes[player1]

        print(player_1, "position:", player1)

        if player1 == 100:
            print("CONGRATS", player_1, "YOU WONNNNN!!! 🎉")
            break


        # Player 2 turn
        input(f"\nPress Enter To Roll The Dice {player_2} ---->")

        dice = random.randint(1,6)
        print("You have rolled:", dice)

        if player2 + dice <= 100:
            player2 += dice
        else:
            print("You need exact number to win")

        if player2 in ladders:
            print("Hurrayyy.. You found a ladder |=|")
            player2 = ladders[player2]

        elif player2 in snakes:
            print("Oops you got bit by a snake... ~~~")
            player2 = snakes[player2]

        print(player_2, "position:", player2)

        if player2 == 100:
            print("CONGRATS", player_2, "YOU WONNNNN!!! 🎉")
            break


    print("\nDo you want to play another game????")
    n = input("Enter yes(y) or no(n): ")

    if n == 'n':
        break

    elif n != 'y':
        break