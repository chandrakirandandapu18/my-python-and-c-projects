while True:
    total = 0

    balls = int(input("Enter number of balls: "))

    if balls > 6:
        print("Maximum 6 balls only")
        continue

    for i in range(1, balls + 1):
        runs = int(input(f"Runs scored in ball {i}: "))

        while runs > 6:
            print("Maximum 6 runs in a ball")
            runs = int(input(f"Runs scored in ball {i}: "))

        total += runs

    print("Total Score =", total)

    again = input("Continue (y/n): ")

    if again == "n":
        break