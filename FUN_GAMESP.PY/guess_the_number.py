guess_ = []
numbers = []

def choose_difficulty():
    if True:
        print("\nChoose Difficulty:")
        print("1. Easy (10 attempts)")
        print("2. Medium (7 attempts)")
        print("3. Hard (5 attempts)")
        choice = int(input("Enter your choice : "))
        match choice:
            case 1:
                return 17
            case 2:
                return 13
            case 3:
                return 7
            case _:
                print("invalid option given..")

attempts = choose_difficulty()

while True:

    while True:
        n = int(input("Enter lenth of number you wanna guess(3-5) : "))
        import random
        match n:
            case 3:
                number = random.randint(100, 1000)
                number = str(number)
                numbers = list(number)
                break

            case 4:
                number = random.randint(1000, 10000)
                number = str(number)
                numbers = list(number)
                break

            case 5:
                number = random.randint(10000, 100000)
                number = str(number)
                numbers = list(number)
                break

            case _:
                print("Inavalid option......")

    final_count = 0

    while True:
        final_count += 1

        if final_count > attempts:
            print("You lost as you did not complete the game in chosen attempts...")
            print("do you want to see the anser ? hahaaaa yes(y) no option unavailable hahaha")
            print(numbers)
            break

        guess = int(input(f"Enter your guess ({n}-digits) :"))
        guess_ = list(str(guess))

        print(guess_)

        def positions():
            i = 0
            while i < n:
                if numbers[i] == guess_[i]:
                    print(f"The number in position {i} is correct !")
                else:
                    print(f"position {i} is not matched ........ !")
                print()
                i = i + 1

        positions()

        def no_of_correct():
            count = 0
            used = []
            i = 0

            while i < n:
                j = 0
                while j < n:
                    if guess_[i] == numbers[j] and j not in used:
                        count = count + 1
                        used.append(j)
                        break
                    j = j + 1
                i = i + 1

            print(f"{count}- digit /digits are correct !!!!\n")

        no_of_correct()

        def repeatitions():
            print("Repeatitions are allowed think carefully......")

        repeatitions()

        if guess_ == numbers:
            print(" Congratulations! You guessed the number!")
            break

    print("\nDo you want to play another game????")
    again = input("Enter yes(y) or no(n): ")

    if again == 'n':
        break
    elif again == 'y':
        print("proceeding.....")
    else:
        print("Invalid answer...!")