import random
player_score=0
computer_score=0
while True:
    input("Press enter to start the the game--->")
    print("====================================")
    print("\tRock-Paper-Scissors")
    print("====================================")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice=int(input("Enter your choice : "))

    if choice==1:
        player='rock'

    elif choice==2:
        player='paper'

    elif choice==3:
        player='scissors'

    else:
        print("invalid choice\npls try again....")
        break

    print("You chose:", player)


    generated=random.randint(1,3)

    if generated==1:
        computer='rock'

    elif generated==2:
        computer='paper'

    elif generated==3:
        computer='scissors'

    else:
        print("invalid choice\npls try again....")
    print("Computer chose:", computer)

    if player=='rock' and computer=='paper':
        print("computer won !!!!")
        computer_score=computer_score+1

    elif player=='paper'and computer=='scissors':
        print("computer won !!!!")
        computer_score=computer_score+1

    elif player=='scissors' and computer=='rock':
        print("computer won !!!!")
        computer_score=computer_score+1

    elif player=='rock' and computer=='rock':
        print("Game draw beacause both chose same option..")

    elif player=='paper' and computer=='paper':
        print("Game draw beacause both chose same option..")

    elif player=='scissors'and computer=='scissors':
        print("Game draw beacause both chose same option..")

    else:
        print("You won !!!!")
        player_score=player_score+1

    again=input("Do you want to play another no(N) and (any key) for yes(Y) : ").upper()
    if again=='N':
        break

    print("===============================")
    print("\tFinal Score")
    print("===============================")

    print("Your score = ",player_score)

    print("computer score = ",computer_score)

if player_score > computer_score :
    print("you won the game ...!!!!")

elif(player_score == computer_score):
    print("Game ended in a draw!")
        
else :
    print("Computer won !")
        

