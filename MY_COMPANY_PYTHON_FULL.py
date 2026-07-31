import random

e_numbers=[]
e_names=[]

while True:
    print("===========================================================")
    print("\t\t---QUATUM EDGE COMPANY---")
    print("===========================================================")

    companies = [
                    "Apple",
                    "Microsoft",
                    "Google",
                    "Amazon",
                    "Meta",
                    "NVIDIA",
                    "OpenAI",
                    "IBM",
                    "Oracle",
                    "Adobe",
                    "Tesla",
                    "Toyota",
                    "BMW",
                    "Mercedes-Benz",
                    "Nike",
                    "Coca-Cola",
                    "Netflix",
                    "Sony",
                    "Tata Consultancy Services",
                    "Reliance Industries"
                ]
    
    def collab():
        i=1
        for company in companies:
                while i<=20:
                    print(f"{i}) " + company, end='\t')
                    i += 1
        print("21)Infosis\n")

    def lunch():
        free_lunch=int(input("Enter your employee number : "))
        if free_lunch in e_numbers:
            print("Here is your lunch sir!")
        else:
            print("Invalid employee number ")

    def e_number():
        e_number=random.randint(1,10000)
        return e_number

    def e_name():
        e_name=input("Enter your name : ")
        return e_name

    def number_guessing_game():
        while True:
            number = random.randint(1, 10)

            guess = 0

            while guess != number:
                guess = int(input("Guess a number (1-10): "))

                if guess < number:
                    print("Too low!")

                elif guess > number:
                    print("Too high!")

                else:
                    print("Congratulations! You guessed the number.")
                
                    again=input("Do you want to play again ? yes(y) or no(n) :")
                    if again=='y':
                        print("playing again...")
                    elif again=='n':
                        break
                    else:
                        print("Invalid option...")

    
    while True:
        want_collabs=input("do you want to see our collabs ? yes(y) or no(n) : ").lower()
        if want_collabs=='y':
            collab()
            break
        elif want_collabs=='n':
            print("OKAY proceeding...")
            break
        else:
            print("Invalid option..")

    research=input("Are you coming to resarch about our company ?yes(y) or no(n) : ").lower()
    match research:
        case 'y':
            def details():
                company_features = [
                                    "HR",
                                    "Finance",
                                    "Sales",
                                    "Marketing",
                                    "IT",
                                    "Employees",
                                    "Projects",
                                    "Attendance",
                                    "Payroll",
                                    "Inventory",
                                    "Customers",
                                    "Reports",
                                    "Meetings",
                                    "Training",
                                    "Security"
                                ]
                for feature in company_features:
                    print(feature)
            details()
        case 'n':
            person=input("Are you a employee(e) or client(c) ? ->").lower()

            if person == 'e':
                exp=input("1)Fresher(F)\n2)old employee(O)\nEnter here : ").lower()

                if exp=='f' or exp=="1":
                    x=e_number()
                    e_numbers.append(x)
                    print("your employee number is ",e_numbers)
                    e_name()

                elif exp=='o' or exp=="2":
                    e_no=int(input("ENter your employee number : "))
                    if e_no in e_numbers:
                        print("Access aproved !!!\nYou can Enter -> ")

                else:
                    print("Invalid response ......!")


                have=input("Do you wan to have lunch ?\nyes(y)\nno(n)\n-> ").lower()
                if have=='y':
                    lunch()
                else:
                    print("Proceeding....")

                game=input("DO YOU WANT TO PLAY GAME yes(y) or no(n) :")
                if game=='y':
                    number_guessing_game()
                else:
                    print("Proceeding....")
                    
            elif person=='c':
                purpose=input("Enter the reason for your occurence sir !\n1)to build projects\n2)for collab\n enter your answer :  ").lower()

                if purpose=='project' or purpose =='projects':
                    print("Welcome !,what project can we build for you sir !")

                elif purpose=='collab' or purpose=='collabration':
                    print("We are happy to collab with you sir ")
                    collab_company=input('Enter your company name sir -> ')
                    companies.append(collab_company)      

                else:
                    print("Invalid response ......!")
            else:
                print("Invalid response ......!")


    