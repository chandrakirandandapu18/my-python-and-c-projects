p=0
try:
    n=int(input("Enter a number in n : "))
    m=int(input("Enter a number in m : "))
    p=n/m

except ZeroDivisionError:
    print("Should not give zero in m ")
    print("ERROR 404")

except ValueError:
    print("Given number should be a integer  ")
    print("ERROR 404")

except SyntaxError:
    print("Pls check the syntax ")

else:
    print("There are no exceptions in your input or code ")
    print("proceeding......")

finally:
    print(f"ans={p}")
    if p==0:
        print("This is the default 'n' value \nThere is a exception in your code")
    else:
        print("Task completed.......")