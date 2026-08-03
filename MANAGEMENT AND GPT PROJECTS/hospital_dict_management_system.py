import random

print("="*35)
print("\t Helix Hospitals")
print("="*35)

data = {}

def patient_no():
    while True:
        number = random.randint(1, 999)
        if number not in [data[x]["patient no"] for x in data]:
            return number

while True:
    print("\n1. Add patient")
    print("2. View patient")
    print("3. Remove patient")
    print("4. Know patient details")
    print("5. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        name = input("Enter patient name : ")
        disease = input("Enter the disease he is suffering from : ")

        number = patient_no()

        data[name] = {
            "patient no": number,
            "disease": disease
        }

        print("Your patient number is:", number)
        print("Patient added successfully.....")


    elif choice == 2:
        name = input("Enter patient name : ")

        if name in data:
            print(data[name])
        else:
            print("Patient not found")


    elif choice == 3:
        name = input("Enter patient name to remove : ")

        if name in data:
            del data[name]
            print("Patient removed successfully")
        else:
            print("Patient not found")


    elif choice == 4:
        name = input("Enter patient name : ")

        if name in data:
            print("Patient Number :", data[name]["patient no"])
            print("Disease :", data[name]["disease"])
        else:
            print("Patient not found")


    elif choice == 5:
        print("Thank you for using Helix Hospitals")
        break


    else:
        print("Invalid choice")

