class student :
    def __init__(self,name,marks,roll_no):
        self.name=name
        self.marks=marks
        self.roll_no=roll_no

    def display(self):
        print("_____student details_____")
        print(f"Name : {self.name}")
        print(f"Marks : {self.marks}")
        print(f"Roll_No : {self.roll_no}")
        print("-------------------------")


s1=student("kiran",100,62001)
s1.display()

s2=student("hemanth",75,72001)
s2.display()

s3=student("navadeep",82,82001)
s3.display()