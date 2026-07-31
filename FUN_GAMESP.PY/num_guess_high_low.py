import random

def choose_difficulty():
    print("\nChoose Difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-500, 5 attempts)")

    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 500, 5
        else:
            print("Invalid choice!")


def play_game():
    max_number, attempts = choose_difficulty()

    number = random.randint(1, max_number)
    score = 100

    print("\nI have selected a number!")
    print(f"Guess between 1 and {max_number}")
    print(f"You have {attempts} attempts.")

    used_attempts = 0

    while used_attempts < attempts:
        try:
            guess = int(input("\nEnter your guess: "))
        except:
            print("Enter a valid number!")
            continue

        used_attempts += 1

        if guess == number:
            score = score - (used_attempts - 1) * 10
            print("\n🎉 Correct!")
            print("Number:", number)
            print("Attempts used:", used_attempts)
            print("Your score:", score)
            return

        elif guess < number:
            print("Too low!")

            if number - guess <= 10:
                print("Hint: You are very close!")

        else:
            print("Too high!")

            if guess - number <= 10:
                print("Hint: You are very close!")

        print("Attempts left:", attempts - used_attempts)

    print("\nGame Over!")
    print("The number was:", number)
    print("Score: 0")


while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ")

    if again.lower() != "yes":
        print("Thanks for playing!")
        break