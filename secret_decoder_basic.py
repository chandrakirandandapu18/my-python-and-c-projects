import os
m=int(input("How many digit password you wanna enter : "))
if m>=10:
    print("password id too big")
else:
    n=int(input(f"Enter a number ({m} digits) : "))
    if len(str(n))==m:
        os.system("cls")
        i=1
        while i<=999999999:
            if i==n:
                print("decoding the password .....")
                print("YOUR Password is ",i)
            i=i+1
    else:
        print("Pls check the no.of digits")
