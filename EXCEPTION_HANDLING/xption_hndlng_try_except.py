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