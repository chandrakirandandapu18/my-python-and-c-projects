file=open("student.txt","w")

n=int(input("Enter no.of students : "))

for i in range(n):
    print(f"Student-{i+1} :")

    roll=int(input("Enter your roll number : "))

    name=input("Enter your name : ")

    marks=float(input("Enter your marks : "))

    file.write(f"Roll Number : {roll}\n")
    file.write(f"Name : {name}\n")
    file.write(f"Marks : {marks}\n\n")
    
file.close()
print("Student record saved succesfully......")
