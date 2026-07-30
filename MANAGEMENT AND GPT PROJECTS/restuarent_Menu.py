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
#----------------------------------------------------------------------------------------------------------------------------------

username = "chandrakirandandapu18@gmail.com"
password = "3101"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")