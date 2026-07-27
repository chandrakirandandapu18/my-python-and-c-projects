while True:
    print("===================================================")
    print("\twelcome to currency converter")
    print("===================================================")
    print("Objective: We will convert Indian Rupees to foreign currencies!")
    print("1. US Dollar ($)")
    print("2. Euro (€)")
    print("3. British Pound (£)")
    print("4. Japanese Yen (¥)")

    currency = int(input("Choose the currency you want to convert into: "))
    ind = int(input("Enter the amount in rupees: "))

    us_dollar = ind / 96
    euro = ind / 111
    pound = ind / 128
    yen = ind / 0.65


    match currency:
        case 1:
            print("Your amount in US Dollar =", us_dollar)
        case 2:
            print("Your amount in Euro =", euro)
        case 3:
            print("Your amount in British Pound =", pound)
        case 4:
            print("Your amount in Japanese Yen =", yen)
        case _:
            print("Invalid choice")

    again=input("Do you want to convert again? yes(y) or no(n) : ").lower()
    if again=='n':
        break
    elif again=='y':
        print("You chose to convert again !")
    else:
        print("inavlid choice")