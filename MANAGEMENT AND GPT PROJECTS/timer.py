import time

n=int(input("Enter a starting number to start the timer : "))
print("Timer starting now !")
while n>=0:
    print(n)
    time.sleep(1)
    n=n-1
print("Times up !")