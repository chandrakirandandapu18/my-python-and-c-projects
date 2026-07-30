num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
#---------------------------------------------------------------------------------------------------------------------------------------
time = int(input("Enter the countdown time: "))

while time > 0:
    print(time)
    time = time - 1

print("Time's Up!")

#---------------------------------------------------------------------------------------------------------------------------------------
age = int(input("Enter your age in years: "))

days = age * 365
months = age * 12
weeks = age * 52
hours = days * 24
minutes = hours * 60
seconds= minutes*60

print("\n----- AGE DETAILS -----")
print("Age:", age, "years")
print("Months:", months)
print("Weeks:", weeks)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds :",seconds)
