import random
import time
while True:
    guess=[]
    score=0
    print("===========================")
    print("\tMemory test")
    print("===========================")
    all_words = [
        "apple", "bridge", "castle", "dragon", "forest",
        "planet", "rocket", "shadow", "river", "mountain",
        "ocean", "pencil", "window", "garden", "flower",
        "camera", "silver", "golden", "basket", "bottle",
        "chair", "table", "cloud", "storm", "light",
        "stone", "clock", "dream", "magic", "sword",
        "shield", "quest", "island", "desert", "jungle",
        "animal", "tiger", "horse", "eagle", "fish",
        "train", "truck", "plane", "phone", "music",
        "movie", "game", "book", "paper", "story"
    ]
    words=random.sample(all_words,5)
    print("YOUR WORDS ARE :")
    print(words)

    time.sleep(5)
    print("\n"*67)

    for i in range(5):
        word=input(f"Enter {i+1} word : ")
        guess.append(word)

    for i in range(5):
        if words[i] == guess[i]:
            score =score+1
    print("\nYour Score:", score, "/5")

    if score == 5:
            print("🔥 Perfect memory!")
    elif score >= 3:
            print("👏 Good memory!")
    else:
            print("😅 Try again!")




    again = input("\nPlay again? (y/n): ").lower()

    if again == "n":
            print("Game Over!")
            break