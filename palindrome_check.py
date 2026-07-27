n=int(input("Enter a number : "))

temp=n

rev=0

while temp>0:

    rev=rev*10+temp%10

    temp=temp//10

if rev==n:
    print("YOUR NUMBER Is PALINDROME NUMBER !!")
else :
    print("ITSS NOT A PALINDOME NUMBER !!")