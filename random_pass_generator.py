import random
import string
characters=string.ascii_letters+string.digits+string.punctuation
password=""
n=int(input("Enter the length of the password :"))
i=1
while i<=n:
    pas=random.choice(characters)
    password=password+pas
    i=i+1
print("Your password is ",password)