num = int(input('Enter your number to check : '))
temp=num
sum = 0



while num > 0 :
    digit = num % 10
    i=1
    fact=1
    while i <= digit :
        fact = fact * i
        i=i+1
    sum = sum + fact 
    num = num // 10

if sum == temp:
    print("Given number is a strong number !")
else:
    print("Given number is not a strong number !")