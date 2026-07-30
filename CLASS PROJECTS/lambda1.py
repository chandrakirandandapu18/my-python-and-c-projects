def square(x):
    return x*x
result=square(5)
print("RESULT=",result)
#--------------------------------------------------------------------------------------------------------------
result1=lambda x:x*x
print(result1(5))
#--------------------------------------------------------------------------------------------------------------
def isEven(y):
    if y%2==0:
        return "even"
    else:
        return "odd"
result2=isEven(7)
print("result2=",result2)
#--------------------------------------------------------------------------------------------------------------
result3= lambda x:"even" if x%2==0 else "odd"
result4=result3(7)
print("result4=",result4)