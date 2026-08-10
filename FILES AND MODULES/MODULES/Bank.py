balance = 12345

def deposit(amount):
    global balance
    balance += amount
    print("Updated Balance:", balance)



def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance")



def check():
    print("Current Balance:", balance)

