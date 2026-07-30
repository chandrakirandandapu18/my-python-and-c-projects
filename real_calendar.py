import calendar
import time
year=int(input("Enter the year : "))
month=int(input("Enter the month :"))
time_line=input("Do you want to view to previous(P) or upcoming(U) years/months :").lower()
while True:
    
   
    print(calendar.month(year,month))
    
    if time_line=='p':
        month=month-1
        if month==0:
            year=year-1
            month=12
            input("Press enter to view next year-->")
    elif time_line=='u':
        month=month+1
        if month==13:
            year=year+1
            month=1
            input("Press enter to view next year-->")
    else:
        print("Invalid choice !")


