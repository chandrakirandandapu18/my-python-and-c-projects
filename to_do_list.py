task=[]
while True:
    print("="*40)
    print("start your to-do list journey")
    print("="*40)
    print("1.note the task")
    print("2.mark the completed task")
    print("3.view all the task")
    print("4.exit")
    print("="*40)
    option=input("choose the option between (1,2,3,4):")
    if option=="exit":
        break
    if option=="1":
       print("="*40)
       print("what task you wanna complete?")
       print("="*40)
       task1=input("Enter your task:")
       print("="*40)
       print("the give task added")
       print("="*40)
       print("task:")
       print(task1)
       print("status:pending")
       task.append(task1)
    elif option=="2":
       print("what task did you complete?")
       task2=input("Enter your task:")
       print("="*40)
       print("The task has completed")
       print("="*40)
       print("task:")
       print(task2)
       print("keep going")
       
    elif option=="3":
        print(task)
    elif option==4:
        break
else: 
    print("invalid . Please choose between options available")