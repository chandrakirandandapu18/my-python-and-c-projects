again = "yes"

while again == "yes" or again == "YES":
    print("Running...")
    again = input("Continue?\nENTER yes or YES or no or NO : ")
    balance=12000
    print("CHECK YOUR BALANCE (1):\nWITHDRAW AMOUNT(2):\nDEPOSIT AMOUNT(3):/n  EXIT :")
    choice=int(input("ENTER YOUR CHOICE :"))
    match choice:
        case 1:
            print("your balance amount is ",balance)
        case 2:
            withdrawing_amount=int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW :"))
            if withdrawing_amount < balance:
                balance=balance-withdrawing_amount
                print("YOUR NEW BALANCE IS ",balance)
            else:
                print("YOUR BALANCE IS LOWER THN THE WITH DRAWAL AMOUNT\nPLS ENTER A VALID AMOUNT")
        case 3:
            deposied_amount=int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT :"))
            balance=balance+deposied_amount
            print("YOUR NEW BALANCE IS ",balance)
        case 4:
            print("YOU HAVE EXITED SUCCESSFULLY")
        case _:
            print('INVALID OPTION,PLS TRY AGAIN')
    again=input("DO YOU WANT TO ENTER AGAIN \nENTER (yes) or (no):")



