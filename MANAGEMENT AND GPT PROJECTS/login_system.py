import random
saved=[]
while True:

    input("Press Enter to login----> ")

    user_name=input("Enter your username : ")
    pas=input("enter your password :")
    if len(pas)<=6:
        print("Weak Password \nYou need a minimum of 7 characters ")
        break

    save=input("Do You want to save the password ? yes(y) or no (n) : "  ).lower()
    if save=='y':
        saved.append(pas)
        print("password saved succesfully....")

    input("Click Enter to generate OTP--->")
    again='y'
    while again=='y':
        otp=random.randint(1000,10000)
        print("your OTP is : ",otp)

        one_time_pass=int(input("Enter the OTP : "))
        if one_time_pass==otp:
            print("OTP Verified")
            break
        else:
            print("Invalid OTP given..")
            print("try again..")
            again=input("Press yes(y) to resend OTP ").lower()
            if again=='n':
                break
    if again=='y':
        print("login successfull")

        see=input("Do You want to see saved the passwords ? yes(y) or no (n) : "  ).lower()
        if see=='y':
            print("Saved passwords are :\n",saved)
        else:
            break
        print("Thank you for visiting our website !!<3")
        break