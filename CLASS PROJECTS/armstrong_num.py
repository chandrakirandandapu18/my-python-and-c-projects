n=int(input("Enter a number : "))

temp=n

digits=len(str(n))

sum=0

while n > 0:
    digit = n % 10
    sum = sum + (digit ** digits)
    n = n//10

if sum == temp:
    print("Given number is a armstrong number !")
else:
    print("Given number is not a armstrong number !")