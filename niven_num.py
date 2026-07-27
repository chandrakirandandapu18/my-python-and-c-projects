n=int(input("Enter a number of your wish : "))
temp=n
sum=0
while n > 0:
    digit=n % 10
    sum =sum + digit
    n = n // 10

if temp % sum == 0:
    print("Given number is a niven number ")
else :
    print("Given number is  not a niven number")