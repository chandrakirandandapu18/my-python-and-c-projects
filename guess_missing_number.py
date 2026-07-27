import random

numbers=[]
while True:

    n=int(input("Enter the maximun number : "))

    for i in range(1,n+1):
        num=numbers.append(i)

    input("Press Enter to start the game ----> ")

    number=random.randint(1,n)

    missing=numbers.remove(number)

    print("your numbers are \n",numbers)

    guess=int(input("Enter the missing number : "))

    if guess==number:
        print("you guessed correct ! yayy!!!")
    else:
        print("guess in corret,try again !")

    again=input("Play again yes(y) ot no(n) : ").lower()
    if again=='n':
        break
