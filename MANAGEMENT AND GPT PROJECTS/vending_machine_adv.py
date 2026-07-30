items = {
    "coke": 40,
    "pepsi": 40,
    "sprite": 35,
    "fanta": 35,
    "water": 20,
    "coffee": 50,
    "tea": 20,
    "chips": 30,
    "chocolate": 25,
    "biscuits": 15,
    "candy": 10,
    "juice": 45,
    "sandwich": 60,
    "burger": 80,
    "pizza slice": 90
}
while True:
    bill=0
    your_items=[]
    i=1

    print("============VENDING MACHINE============")

    for item, price in items.items():
        print(f"{item:<13}= {price} rupees")

    n=int(input("How many items you wanna buy ? -> "))
    while i<=n:

        choice=input(f"Enter item no {i}  -> ").lower()
        if choice in items:
            money=items[item]
            bill=bill+money
            your_items.append(choice)
        else:
            print("Items not available >>>!")
        i=i+1

    print("your items are : ",your_items)
    print("BILL : ",bill)

    again=input("Do you want to buy again yes(y) or no (N) : ")
    if again=='n':
        break
    elif again=='y':
        print("You chose to buy again !")
    else:
        print("invalid choice......")
