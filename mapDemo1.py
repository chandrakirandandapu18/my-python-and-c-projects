def square(x):
    return x*x
map_obj=map(square,[6,7,8,9])
result=list(map_obj)
print("result=",result)
#---------------------------------------------------------------------------------------------------------------
def square(y):
    return y*y
map_obj2=map(square,[6,7,8,9])
for i in map_obj2:
    print(i)
#----------------------------------------------------------------------------------------------------------------
def square(z):
    return z*z
map_obj3=map(square,[6,7,8,9])
l1=[1,2,3,4]
i=0
while i<len(l1):
    print(l1[i])
    i=i+1
