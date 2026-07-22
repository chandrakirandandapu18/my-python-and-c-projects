score = 0

print("===== MATHS & LOGIC QUIZ GAME =====")

# Question 1
print("\n1. What is 15 + 25?")
print("A. 30")
print("B. 40")
print("C. 50")
print("D. 45")

ans = input("Enter your answer (A/B/C/D): ").upper()

if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
print("\n2. If 5 machines make 5 items in 5 minutes, how long will 1 machine take to make 1 item?")
print("A. 1 minute")
print("B. 5 minutes")
print("C. 10 minutes")
print("D. 25 minutes")

ans = input("Enter your answer: ").upper()

if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
print("\n3. What comes next? 2, 4, 8, 16, ?")
print("A. 20")
print("B. 24")
print("C. 32")
print("D. 36")

ans = input("Enter your answer: ").upper()

if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 4
print("\n4. A train travels 60 km in 1 hour. How far will it travel in 3 hours?")
print("A. 120 km")
print("B. 150 km")
print("C. 180 km")
print("D. 200 km")

ans = input("Enter your answer: ").upper()

if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 5
print("\n5. If CAT = 3120, then DOG = ?")
print("A. 4157")
print("B. 4715")
print("C. 4156")
print("D. 5147")

ans = input("Enter your answer: ").upper()

if ans == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n====================")
print("Your Score:", score, "/5")

if score == 5:
    print("🔥 Perfect Score! Genius!")
elif score >= 3:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")