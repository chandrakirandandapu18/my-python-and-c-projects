def welcome():
    print("==============================")
    print("       GENERAL QUIZ")
    print("==============================")


def show_rules():
    print("\nRULES:")
    print("1. There are 5 questions.")
    print("2. Each correct answer gives 1 point.")
    print("3. Enter A, B, C or D.")


def ask_question(question, options, correct_answer):
    print("\n" + question)

    for option in options:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        print("Correct answer:", correct_answer)
        return 0


def show_score(score):
    print("\n==============================")
    print("          RESULT")
    print("==============================")

    print("Your score:", score, "/ 5")

    if score == 5:
        print("Excellent! 🔥")
    elif score >= 3:
        print("Good job!")
    else:
        print("Keep practicing!")


def start_quiz():
    score = 0

    score += ask_question(
        "1. Which language is known as a systems programming language?",
        ["A. HTML", "B. C", "C. SQL", "D. CSS"],
        "B"
    )

    score += ask_question(
        "2. Which keyword is used to create a function in Python?",
        ["A. function", "B. create", "C. def", "D. fun"],
        "C"
    )

    score += ask_question(
        "3. Which symbol is used for comments in Python?",
        ["A. //", "B. /* */", "C. #", "D. <!-- -->"],
        "C"
    )

    score += ask_question(
        "4. Which data type stores True or False?",
        ["A. int", "B. bool", "C. float", "D. str"],
        "B"
    )

    score += ask_question(
        "5. Which loop is commonly used to iterate over a sequence?",
        ["A. for", "B. switch", "C. goto", "D. case"],
        "A"
    )

    return score


welcome()
show_rules()

input("\nPress Enter to start...")

final_score = start_quiz()

show_score(final_score)
