marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")
#---------------------------------------------------------------------------------------------------------------
i=1
while i==1:
    a=float(input("enter a number :"))
    b=float(input("enter another number:"))
    print("ADDIION(1):\nSUBTRACTION(2):\nMULTIPLICATION(3):\nDIVISION(4):")
    c=int(input("enter the type of calculation (1) or (2) or (3) or (4):"))
    if c==1:
        result1=a+b
        print("addition of given numbers is :",result1)
    elif c==2:
        result2=a-b
        print("subtraction of given numbers is:",result2)
    elif c==3:
        result3=a*b
        print("after multiplicattion result is :",result3)
    elif c==4:
        if b!=0:
            e=input("you want the demimals ? enter yes or no(all caps) :")
            if e=="NO":
                result5=a//b
                print('after floor division :',result5)
            else:
                result4=a/b
                print("after divion result:",result4)
        else:
            print("\ndivision with zero is undefined")
    else:
        print("given invalid number,try again")
    i=int(input("enter '1' to do agian and '2' to quit calculator :"))



