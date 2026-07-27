n=int(input("what number factorial do you want : "))
i=1
factorial=1
while i<=n:
    factorial=factorial*i
    i=i+1
print(f"factorial of {n} is ",factorial)