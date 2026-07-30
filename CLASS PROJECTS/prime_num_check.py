n=int(input("enter a number : "))
i=1
count=0
while i <= n:
    if n%i==0:
        print("factors are ",i)
        count=count+1
    i=i+1

if count==2:
    print("Given number is a prime number " )
else:
    print("Given number is not a prime number ")