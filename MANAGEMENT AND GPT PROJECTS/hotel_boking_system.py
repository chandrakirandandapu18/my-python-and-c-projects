rooms = ["101", "102", "103", "104", "105",
         "106", "107", "108", "109", "110",
         "201", "202", "203", "204", "205",
         "206", "207", "208", "209", "210",
         "301", "302", "303", "304", "305",
         "306", "307", "308", "309", "310"]

while True:
    print("\n===== HOTEL BOOKING =====")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Rooms:")
        for room in rooms:
            print(room,end=' ')

    elif choice == 2:
        room = input("Enter room number: ")

        if room in rooms:
            rooms.remove(room)
            print("Room booked successfully!")
        else:
            print("Room not available!")

    elif choice == 3:
        print("Thank you! Visit Again.")
        break

    else:
        print("Invalid Choice!")
