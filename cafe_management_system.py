print("============================")
print("\tROYAL CAFE")
print("============================")
bill=0
input("Press Enter to order ---->")
menu = {
    "coffee": 120,
    "cappuccino": 180,
    "espresso": 150,
    "latte": 200,
    "mocha": 220,
    "hot Chocolate": 180,
    "tea": 80,
    "green Tea": 100,
    "lemon Tea": 90,
    "cold Coffee": 200,
    "milkshake": 250,
    "smoothie": 280,
    "burger": 180,
    "vheese Burger": 220,
    "veg Sandwich": 150,
    "grilled Sandwich": 190,
    "french Fries": 140,
    "garlic Bread": 130,
    "pizza": 350,
    "pasta": 280,
    "noodles": 240,
    "brownie": 160,
    "ice Cream": 120,
    "donut": 90,
    "muffin": 100
}
for item in menu:
    print(item,"=",menu[item])

while True:
    first=input("what whould you like to order ? ->").lower()
    if first in menu:
        price=menu[item]
        bill=bill+price
    else:
        print("item is not available !")

    re_order=input("Do you want anything else ? yes(y) or no (n) : ")
    if re_order=='n':
        break
print(f"YOUR BILL : {bill} ")
payment=input("cash(m) or card(c) ?").lower()
if payment=='m':
    amount=int(input("Enter your amaount : "))
    if amount<bill:
            remaining=bill-amount
            print(f"YOU still need to pay {remaining} rupees ! ")
            pay=int(input("Enter remaining money :"))
            if pay==remaining:
                print("thank you for vistiting sir")
            elif pay<remaining:
                 print("pls pay the coreect amount or we will take serious action !")
                 reremaining=remaining-pay
                 repay=int(input(f"Enter {reremaining} rupees  :"))
                 if repay!=reremaining:
                      print("you are under arrest !")
    if amount==bill:
         print("thank you for vistiting sir")
    if amount>bill     :
         print("Thankyou for ur tip !")
         print("thank you for vistiting sir")
if payment=='c':
    amount=int(input("Enter your amaount : "))
    if amount<bill:
                 remaining=bill-amount
                 print(f"YOU still need to pay {remaining} rupees ! ")
                 pay=int(input("Enter remaining money :"))
                 if pay==remaining:
                     print("thank you for vistiting sir")
                 elif pay<remaining:
                      print("pls pay the coreect amount or we will take serious action !")
                      reremaining=remaining-pay
                      repay=int(input(f"Enter {reremaining} rupees  :"))
                      if repay!=reremaining:
                           print("you are under arrest !")
    if amount==bill:
              print("thank you for vistiting sir")
    if amount>bill :
              print("Thankyou for ur tip !")
              print("thank you for vistiting sir")
        