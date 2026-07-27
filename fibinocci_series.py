n=int(input("ENTER UPTO WHAT NUMBER YOU WANT THE SERIES TO END ! : "))

count=0

first=0

second=1

while count<n:
    print(first)

    next=first+second

    first=second

    second=next

    count=count+1