si=lambda p,t,r:(p*t*r)/100
print(si(10,20,30))
#----------------------------------------------------------------------------------------------------------------
leap=lambda year:"leap year" if (year % 400 ==0 or year % 4 ==0 and year % 100 !=0) else "not a leap year"
print(leap(2025))