print("1. All Caps")

print("2. FirstLetter Cap")

print("3. All lower_case")

choice=int(input("Enter a number : "))

script=input("Write your msg :\n")
match choice:
    case 1:
        script=script.upper()
        print(script)

    case 2:
        sep=list(script)
        
        sep[0]=sep[0].upper()
        
        script="".join(sep)
        print(script)

    case 3:
        script=script.lower()
        print(script)

    case _:
        print("Invalid option....")
