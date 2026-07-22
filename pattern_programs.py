print("1. square")
print("2. right angled triangle")
print("3. triangle")
print("4. diamond")
choose=int(input("Enter the shape you want to create : "))
if choose==1:
    n = int(input("\nEnter size: "))
    i=0
    while i<n :
        j=0
        while j<n :
            print("*",end=" ")
            j=j+1
        print()
        i=i+1
print("===================================================================================================================================")
if choose==2:
    n = int(input("Enter size: "))
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print("*", end=" ")
            j = j + 1
        print()
        i = i + 1
print("===================================================================================================================================")
if choose==3:
    n = int(input("\nEnter size: "))
    i=1
    while i<=n:
        j=1
        while j<=n-i:
            print(" ",end=' ')
            j=j+1
        k=1
        while k<=(2 * i - 1):
            print("*",end=' ')
            k=k+1
        print()
        i=i+1
print("===================================================================================================================================")
if choose==4:
    n = int(input("\nEnter size: "))
    i=1
    while i<=n:
        j=1
        while j<=n-i:
            print(" ",end=' ')
            j=j+1
        k=1
        while k<=(2 * i - 1):
            print("*",end=' ')
            k=k+1
        print()
        i=i+1
    i=n-1
    while i>=1:
        j=1
        while j<=n-i:
            print(" ",end=' ')
            j=j+1
        k=1
        while k<=(2 * i - 1):
            print("*",end=' ')
            k=k+1
        print()
        i=i-1
    print("===================================================================================================================================")
else:
    print("invalid option")