
n=int(input("Enter a number : "))
temp=n

sum=0
while n > 0 :
    fact=1
    i=1
    digit=n % 10
    while i <= digit :
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if sum == temp:
    print("It is a strong number...")
else:
    print("It is not a strong number...")

#-----------------------------------------------------------------------------------------------------------------------------------

x=int(input("Enter a number : "))
i=1
sum=0
while i < x :
    if x % i == 0:
        sum=sum+i
    i=i+1
if sum == x:
    print("It is a perfect number...")
else:
    print("it is not a perfect number....")

