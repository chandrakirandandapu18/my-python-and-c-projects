import random
score=0
words = [
        "apple",
        "mango",
        "grape",
        "chair",
        "table",
        "house",
        "water",
        "money",
        "phone",
        "school",
        "orange",
        "banana",
        "pencil",
        "garden",
        "bottle",
        "window",
        "flower",
        "rabbit",
        "tiger",
        "monkey"
    ]
print(words)
while True:
    
    word=random.choice(words) #choose a element from non empty thing
    letters=list(word) 
    random.shuffle(letters)
    scrambled="".join(letters)
    print("here is your scrambled word :",scrambled)
    guess=input("enter your guess : ").lower()
    if word==guess:
        print("you are corect !!!")
        score=score+1
        print("'+1 point'")
    else:
        print("you guessed wrong !")
        print("+0 points")
    again=input("do you want to continue again? yes(y) or no(n) :").lower()
    if again=='n':
            print("===============================")
            print("\tFinal Score")
            print("===============================")
            print("your score = ",score)
            break
    else:
        print("invalid choice")
    
    print("===============================")
    print("\tFinal Score")
    print("===============================")
    print("your score = ",score)