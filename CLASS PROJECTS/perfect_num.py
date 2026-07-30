n=int(input("Enter the number that you wanna check as a perfect number : "))

temp=n

sum=0
i=1
while i < n :

    if n % i== 0 :

        sum=sum + i

    i=i+1

if sum==temp:
        print("YOUR NUMBER IS A PERFECT NUMBER !")
else:
        print("YOUR NUMBER IS NOT A PERFECT NUMBER !")