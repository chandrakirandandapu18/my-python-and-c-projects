file = open("student.txt", "r")


print("Student Records")
print("----------------")

while True:
    roll = file.readline()

    if roll == "":
        break

    name = file.readline()
    marks = file.readline()
    file.readline()   # skips the blank line

    roll = roll.replace("Roll Number : ", "").strip()
    name = name.replace("Name : ", "").strip()
    marks = float(marks.replace("Marks : ", "").strip())

    print("Roll Number :", roll)
    print("Name        :", name)
    print("Marks       :", marks)
    print()



file.close()

