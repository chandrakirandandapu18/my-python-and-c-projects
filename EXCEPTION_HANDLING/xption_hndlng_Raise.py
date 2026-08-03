age = -5

if age < 0:
    raise ValueError("Age cannot be negative")

print("================================================================================================================")
marks = 120

if marks > 100:
    raise ValueError("Marks cannot exceed 100")

print("================================================================================================================")
password = input("Enter password: ")

if len(password) < 8:
    raise ValueError("Password must be at least 8 characters")

try:
    name = 123

    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    print(name)

except TypeError as e:
    print(e)

print("================================================================================================================")
balance = 500
amount = 1000

try:
    if amount > balance:
        raise Exception("Insufficient balance")

    print("Transaction successful")

except Exception as e:
    print(e)
print("================================================================================================================")