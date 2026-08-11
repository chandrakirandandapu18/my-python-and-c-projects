student_names = []
student_numbers = []

print("==========================================")
print("          SCHOOL MANAGEMENT SYSTEM")
print("==========================================")

student = input("Are you a student? yes/no : ").lower()


# ================= STUDENT =================

if student == "yes":

    print("\n..... WELCOME STUDENT .....")

    name = input("Enter your name: ")
    student_names.append(name)

    student_number = int(input("Enter your student number: "))
    student_numbers.append(student_number)

    student_class = int(input("Enter your class: "))

    print("\n========== STUDENT DETAILS ==========")
    print("Name:", name)
    print("Student Number:", student_number)
    print("Class:", student_class)
    print("Attendance: PRESENT")

    print("\nYou are marked as present.")
    print("Now go to your class.....")


# ================= PARENT / TEACHER =================

elif student == "no":

    print("\n========== SELECT USER ==========")
    print("1. Parent")
    print("2. Teacher")

    select = int(input("Enter the selection: "))


    # ================= PARENT =================

    if select == 1:

        print("\n..... WELCOME PARENT .....")
        print("How can we help you?")

        print("\n1. Student Details")
        print("2. Fee Payment")
        print("3. Permission for Home")
        print("4. School Information")

        choice = int(input("Enter your choice: "))


        match choice:


            # ========== STUDENT DETAILS ==========

            case 1:

                print("\n========== STUDENT DETAILS ==========")

                student_number = int(input("Enter student number: "))
                student_numbers.append(student_number)

                student_name = input("Enter student name: ")
                student_names.append(student_name)

                marks = int(input("Enter marks: "))

                print("\nStudent Number:", student_number)
                print("Student Name:", student_name)
                print("Marks:", marks)

                if marks >= 90:
                    print("Grade: A+")
                    print("Excellent! Your performance is outstanding.")

                elif marks >= 80:
                    print("Grade: A")
                    print("Very good! Keep up the excellent work.")

                elif marks >= 70:
                    print("Grade: B")
                    print("Good job! You are doing well.")

                elif marks >= 60:
                    print("Grade: C")
                    print("Decent performance, but you can improve.")

                elif marks >= 50:
                    print("Grade: D")
                    print("You passed, but you need to work harder.")

                else:
                    print("Grade: F")
                    print("You failed. Don't give up, work harder and try again.")


            # ========== FEE PAYMENT ==========

            case 2:

                print("\n========== SCHOOL FEE STRUCTURE ==========")

                student_name = input("Enter student name: ")
                student_class = int(input("Enter your class: "))

                if student_class == 1:
                    fee = 25000

                elif student_class == 2:
                    fee = 27000

                elif student_class == 3:
                    fee = 29000

                elif student_class == 4:
                    fee = 31000

                elif student_class == 5:
                    fee = 33000

                elif student_class == 6:
                    fee = 35000

                elif student_class == 7:
                    fee = 37000

                elif student_class == 8:
                    fee = 39000

                elif student_class == 9:
                    fee = 41000

                elif student_class == 10:
                    fee = 43000

                else:
                    fee = 0

                if fee != 0:

                    print("\nStudent:", student_name)
                    print("Class:", student_class)
                    print("Total Fee: ₹", fee)

                    payment = input(
                        "Do you want to pay the fee? yes(y)/no(n): "
                    ).lower()

                    if payment == "yes":
                        print("Fee payment successful.")
                        print("Thank you for the payment.")

                    elif payment == "no":
                        print("Fee payment cancelled.")

                    else:
                        print("Invalid payment option.")

                else:
                    print("Invalid class!")


            # ========== HOME PERMISSION ==========

            case 3:

                print("\n========== PERMISSION FOR HOME ==========")

                print("1. He is feeling unwell.")
                print("2. He has a doctor's appointment.")
                print("3. There is a family emergency.")
                print("4. He has an important family matter.")
                print("5. He has an urgent school-related appointment.")
                print("6. Other")

                reason = int(input("Enter the reason number: "))

                if reason == 1:
                    print("Reason: He is feeling unwell.")
                    print("Permission granted.")

                elif reason == 2:
                    print("Reason: He has a doctor's appointment.")
                    print("Permission granted.")

                elif reason == 3:
                    print("Reason: There is a family emergency.")
                    print("Permission granted.")

                elif reason == 4:
                    print("Reason: He has an important family matter.")
                    print("Permission granted.")

                elif reason == 5:
                    print("Reason: He has an urgent school-related appointment.")
                    print("Permission granted.")

                elif reason == 6:
                    print("Permission not granted.")
                    print("Please provide a valid reason.")

                else:
                    print("Invalid reason number.")


            # ========== SCHOOL INFORMATION ==========

            case 4:

                print("\n========== SCHOOL INFORMATION ==========")

                print("School Name: ABC International School")
                print("School Timing: 8:30 AM - 3:30 PM")
                print("Principal: Mr. John")
                print("Office Timing: 9:00 AM - 4:00 PM")
                print("Contact: 9876543210")

                print("\nThank you for contacting the school.")


            case _:
                print("Invalid choice!")


    # ================= TEACHER =================

    elif select == 2:

        print("\n..... WELCOME TEACHER .....")

        print("\n1. Mark Attendance")
        print("2. Check Student")
        print("3. Enter Marks")
        print("4. Check Student Performance")

        teacher_choice = int(input("Enter your choice: "))


        match teacher_choice:


            # ========== ATTENDANCE ==========

            case 1:

                print("\n========== ATTENDANCE ==========")

                student_name = input("Enter student name: ")

                attendance = input(
                    "Is the student present? yes(y)/no(n): "
                ).lower()

                if attendance == "yes":
                    print(student_name, "is marked PRESENT.")

                elif attendance == "no":
                    print(student_name, "is marked ABSENT.")

                else:
                    print("Invalid attendance option.")


            # ========== CHECK STUDENT ==========

            case 2:

                print("\n========== CHECK STUDENT ==========")

                student_number = int(input("Enter student number: "))
                student_name = input("Enter student name: ")

                print("\nStudent Number:", student_number)
                print("Student Name:", student_name)
                print("Student record checked successfully.")


            # ========== ENTER MARKS ==========

            case 3:

                print("\n========== ENTER MARKS ==========")

                student_name = input("Enter student name: ")
                marks = int(input("Enter marks: "))

                print("\nStudent:", student_name)
                print("Marks:", marks)

                if marks >= 90:
                    print("Grade: A+")
                    print("Outstanding performance.")

                elif marks >= 80:
                    print("Grade: A")
                    print("Excellent performance.")

                elif marks >= 70:
                    print("Grade: B")
                    print("Good performance.")

                elif marks >= 60:
                    print("Grade: C")
                    print("Decent performance.")

                elif marks >= 50:
                    print("Grade: D")
                    print("Needs improvement.")

                else:
                    print("Grade: F")
                    print("Student has failed.")


            # ========== PERFORMANCE ==========

            case 4:

                print("\n========== STUDENT PERFORMANCE ==========")

                student_name = input("Enter student name: ")
                marks = int(input("Enter marks: "))
                attendance = int(input("Enter attendance percentage: "))

                print("\nStudent:", student_name)

                if marks >= 50 and attendance >= 75:
                    print("Status: GOOD")
                    print("Student is eligible for promotion.")

                elif marks >= 50 and attendance < 75:
                    print("Status: WARNING")
                    print("Marks are good, but attendance is low.")

                elif marks < 50 and attendance >= 75:
                    print("Status: NEEDS IMPROVEMENT")
                    print("Attendance is good, but marks are low.")

                else:
                    print("Status: POOR")
                    print("Student needs improvement in both marks and attendance.")


            case _:
                print("Invalid teacher choice!")


    else:
        print("Invalid selection!")


else:
    print("\nInvalid input!")
    print("Please enter yes(y) or no(n).")


print("\n==========================================")
print("       THANK YOU FOR USING THE SYSTEM")
print("==========================================")