contacts = []
numbers = []

while True:
    print("=====================================")
    print("\tWELCOME TO CONTACT LIST")
    print("=====================================")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        c_number = input("Enter the number: ")

        if len(c_number) != 10:
            print("Please enter a 10-digit number.")
        else:
            numbers.append(c_number)
            name = input("Enter contact name: ")
            contacts.append(name)
            print("Contact added successfully!")

    elif choice == 2:
        print(contacts)

    elif choice == 3:
        view = input("Enter the contact name to search: ")

        if view in contacts:
            print("This contact is available.")
        else:
            print("Contact not found.")

    elif choice == 4:
        break
    else:
        print("404 ERROR \n pls choose from 1-4 numbers only ")
