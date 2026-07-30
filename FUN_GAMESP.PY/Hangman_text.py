import random
while True:
    verbs = [
    "accept", "achieve", "acquire", "adjust", "advise",
    "afford", "agree", "allow", "announce", "appear",
    "apply", "argue", "arrange", "assist", "avoid",
    "balance", "belong", "borrow", "bounce", "capture",
    "change", "charge", "choose", "climb", "collect",
    "compare", "complete", "connect", "create", "dance",
    "decide", "deliver", "depend", "describe", "develop",
    "discover", "divide", "escape", "explain", "explore",
    "follow", "forget", "gather", "handle", "happen",
    "imagine", "improve", "include", "invite", "listen",
    "manage", "measure", "mention", "notice", "observe",
    "perform", "prepare", "prevent", "produce", "protect",
    "provide", "receive", "repair", "repeat", "return",
    "search", "select", "share", "shout", "solve",
    "spend", "start", "travel", "trust", "unlock",
    "update", "upload", "verify", "visit", "watch",
    "write", "learn", "teach", "think", "understand",
    "welcome", "wonder", "worry", "survive", "support"
]
    word=random.choice(verbs)
    final_guess = ["_"] * len(word)
    letters=list(word)
    count=0

    length=len(word)
    print("HINT : your letter is a verb !!")
    print(f"No.of letters in your word is {length}")
    while True:
        guess=input("guess a letter--> ")
        count=count+1
        if guess in letters:
            position=letters.index(guess)

            print("given letter is in the word !!\n")

            print(f"your letter is in position {position} !\n")

            final_guess[position] = guess
            print(final_guess)

        else:
            print("Guessed letter is not in the word,unfortunately!!!\n")
           
        if count>=30:
            print("you took a lot of turns try again !!\n you lost!!")
            break
        
        if final_guess==letters:
            print("hurray u found the letter ! yayy!!\n")
            break

    again=input("Do you want to play again ?\nyes(y) or no(n)")
    if again=='n':
        break