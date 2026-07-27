passwords = {}

while True:
    print("\n--- Password Saver ---")
    print("1. Add Password")
    print("2. View Password")
    print("3. Delete Password")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        website = input("Enter website/app name: ")
        password = input("Enter password: ")

        passwords[website] = password
        print("Password saved!")

    elif choice == 2:
        website = input("Enter website/app name: ")

        if website in passwords:
            print("Password:", passwords[website])
        else:
            print("No password found!")

    elif choice == 3:
        website = input("Enter website/app name: ")

        if website in passwords:
            del passwords[website]
            print("Password deleted!")
        else:
            print("No password found!")

    elif choice == 4:
        print("Exiting Password Saver...")
        break

    else:
        print("Invalid choice!")
