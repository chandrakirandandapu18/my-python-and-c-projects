import time
import os
print("RED LIGHT ")
i=1
while i<=45:
    print(i)
    time.sleep(1)
    i=i+1
print("YELLOW LIGHT")
k=1
while k<=3:
    print(k)
    k=k+1
print("GREEN LIGHT")
j=1
while j<=20:
    print(j)
    j=j+1

#----------------------------------------------------------------------------------------------------------------------------------------
import random
h="heads"
t="tails"
coin=("HEADS","TAILS")

toss=random.choice(coin)
print(toss)
