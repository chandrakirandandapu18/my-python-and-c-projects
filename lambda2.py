a=int(input("ENTER A NUMBER :"))
b=int(input("ENTER A DIFFERENT NUMBER :")) 
c=int(input("ENTER A NUMBER :")) 
def max(a,b):
    if a>b:
        print("a is maximum\n")
    else:
        print(" b is maximum\n")
max(a,b)
#----------------------------------------------------------------------------------------------------------------
max=lambda x,y: x if x>y else y
maximum=max(10,20)
print("mximum=",maximum)
#-----------------------------------------------------------------------------------------------------------------
maxi=lambda a,b,c:a if a>b and a>c else (b if b>c else c)
result3=maxi(a,b,c)
print("\nreslut3=",result3)
