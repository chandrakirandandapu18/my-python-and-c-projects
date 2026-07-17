#funtions with arguments and with return type
def addition(a,b):
    c=a+b
    return c
print(addition(10,20))
#-------------------------------------------------------------------------------------------------------
#funtions with arguments and without return type
def subtraction(x,y):
    z=x-y
    print("z=",z)
subtraction(18,17)
#-------------------------------------------------------------------------------------------------------
#funtions without arguments amd with return type
def multiplication():
    p=int(input("enter a value in 'p' :"))
    q=int(input("enter a value in 'q' :"))
    r=p*q
    return r
print(multiplication())
#-------------------------------------------------------------------------------------------------------
#funtions without arguments and without return type
def division():
    e=1234
    f=567
    g=e/f
    print("g=",g)
division()
