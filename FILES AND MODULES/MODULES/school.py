def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

def display(name, roll, avg):
    print("\n----- Student Details -----")
    print("Name :", name)
    print("Roll :", roll)
    print("Average :", avg)
    print("Grade :", grade(avg))