total = 0
print("Welcome to the Restaurant Menu")
print("------------------------------")
print("------ MENU ------")
print("1. Burger      - ₹120")
print("2. Pizza       - ₹250")
print("3. Sandwich    - ₹80")
print("4. Fries       - ₹90")
print("5. Pasta       - ₹180")
print("6. Coke        - ₹40")
print("7. Coffee      - ₹60")
print("8. Tea         - ₹20")
print("9. Ice Cream   - ₹70")
print("10. Water      - ₹20")

while True:
    price = int(input("Enter item price (0 to stop): "))

    if price == 0:
        break

    total = total + price

print("Total Bill =", total)
total = 0
#----------------------------------------------------------------------------------------------------------------------------------
balls = int(input("Enter number of balls: "))
if(balls > 6):
    print("You can only enter a maximum of 6 balls.")

for i in range(1, balls + 1):
    runs = int(input(f"Runs scored in {i} ball : "))
    if(runs > 6):
        print("You can only score a maximum of 6 runs in a ball.")
        runs = int(input(f"Runs scored in {i} ball : "))
    total = total + runs

print("Total Score =", total)
#----------------------------------------------------------------------------------------------------------------------------------
username = "chandrakirandandapu18@gmail.com"
password = "3101"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")