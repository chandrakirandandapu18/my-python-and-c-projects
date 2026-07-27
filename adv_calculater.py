def calculator():
    expression = input("Enter calculation: ")

    result = eval(expression)

    print("Answer =", result)


while True:
    print("\n1. Calculate")
    print("2. Exit")

    choice = int(input("Choose: "))

    if choice == 1:
        calculator()

    elif choice == 2:
        print("Calculator closed")
        break

    else:
        print("Invalid choice")