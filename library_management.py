while True:
    print("=========================================")
    print("\tWelcome to the library")
    print("=========================================")
    print("BOOKS AVAILABLE RN ARE : ")
    library = {
        "Python Basics": 450,
        "C Programming": 380,
        "Java Programming": 520,
        "Data Structures": 650,
        "Operating Systems": 700,
        "Computer Networks": 600,
        "DBMS": 550,
        "Machine Learning": 900,
        "Web Development": 750,
        "Artificial Intelligence": 950
    }
    print(library)
    print("1.RENT A BOOK :")
    print("2.RETURN A BOOK :")
    print("3.BUY A BOOK :")
    print("4.EXIT")
    choice=int(input("ENTER YOUR CHOICE : "))
    match choice:
        case 1:
            print("THE PRICE TO RENT A BOOK IS 200 rupees ")
            book=input("ENTER WHAT BOOK U WANT :")
            if book in library:
                print("here you go ma'am/sir ")
            else:
                print("THE BOOK U WANT IS NOT NOT AVAILABLE,sorryy.....")
        case 2:
            book=input("ENTER THE BOOK U WERE RETURNING : ")
            if book in library:
                print("THANK YOU FOR RETURNING SIR")
            else:
                print("THIS BOOK IS NOT FROM OUR LIBRARY")
        case 3:
            book=input("ENTER THE BOOK U WANNA BUY : ")
            if book in library:
                cost=int(input("pls enter the cost as per book menu sir : "))
                print(cost,"pls handover cash to counter ")
                print("thank u from buying book from our laptop sir.... ")
            else :
                print("THE BOOK U R SEARCHING FOR IS NOT AVAILABLE IN OUR LIBRARY SIR\n WE ARE EXTREMELY SORRYY...........")
        case 4:
            print("YOU CHOSE TO EXIT THE LIBRARY ")
            break
    sug=input("if you want us to add books pls enter your suggestions \n are you willing to yes(y) or no(n) : ")
    if sug=='y':
        sug=input("ENTER YOUR SUGGESTIONS : ")
    print("THANK U FOR CHOOSING OUR SERVICE ")

    
    