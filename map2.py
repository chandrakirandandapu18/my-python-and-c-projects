def sum(a,b):

    return a+b
obj=map(sum,(12,34,56,78),[12,23,34,45])
result=list(obj)
print(result)
#-------------------------------------------------------------------------------------------------------------
def long_sum(a,b,c):
    return a+b+c
map_obj=map(long_sum,[45,9378,86,965],[712,9230,345],(234,876,99,109))
result2=list(map_obj)
print(result2)