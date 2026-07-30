a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print(a, "is the largest.")
    else:
        print(c, "is the largest.")
else:
    if b > c:
        print(b, "is the largest.")
    else:
        print(c, "is the largest.")
#---------------------------------------------------------------------------------------------------------------
pin = int(input("Enter your PIN: "))

if pin == 1234:
    balance = float(input("Enter your balance: "))
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")
#------------------------------------------------------------------------------------------------------------------
marks = int(input("Enter your marks: "))

if marks >= 35:
    if marks >= 90:
        print("Grade A+")
    else:
        if marks >= 75:
            print("Grade A")
        else:
            if marks >= 60:
                print("Grade B")
            else:
                print("Grade C")
else:
    print("Fail")