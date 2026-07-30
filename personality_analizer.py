print("----- PERSONALITY ANALYZER -----")
def one():
    print("\nQuestion 1:")
    print("You are given a problem nobody has solved before. What do you do first?")
    print("A) Break it into smaller parts and analyze everything")
    print("B) Experiment with different solutions")
    print("C) Think of a completely new approach")
    print("D) Ask someone experienced for guidance")
    ans=input("enter your option").lower()
    if ans!= 'a' and ans!='b' and ans!='c' and ans!='d':
        print("INVALID OPTION")
    return ans
result0=one()
print(result0)

def two():
    print("\nQuestion 2:")
    print("You get one month of free time. What would you choose?")
    print("A) Learn a difficult skill")
    print("B) Build a personal project")
    print("C) Explore new experiences")
    print("D) Improve something you already know")
    ans=input("enter your option").lower()
    if ans!= 'a' and ans!='b' and ans!='c' and ans!='d':
        print("INVALID OPTION")
    return ans
result1=one()
print(result1)

def three():
    print("\nQuestion 3:")
    print("Your idea gets criticized by someone. What is your reaction?")
    print("A) Check if their points are logically correct")
    print("B) Use it as motivation to improve")
    print("C) Think of a better version of your idea")
    print("D) Ask more people for opinions")
    ans=input("enter your option").lower()
    if ans!= 'a' and ans!='b' and ans!='c' and ans!='d':
        print("INVALID OPTION")
    return ans
result2=two()
print(result2)

def four():
    print("\nQuestion 4:")
    print("Your team cannot agree on a solution. You:")
    print("A) Choose the option with the strongest reasoning")
    print("B) Take responsibility and make a decision")
    print("C) Combine everyone's ideas into a new solution")
    print("D) Help the team reach an agreement")
    ans=input("enter your option").lower()
    if ans!= 'a' and ans!='b' and ans!='c' and ans!='d':
        print("INVALID OPTION")
    return ans
result3=three()
print(result3)

def five():
    print("\nQuestion 5:")
    print("What gives you the most satisfaction?")
    print("A) Understanding complex things")
    print("B) Achieving difficult goals")
    print("C) Creating something unique")
    print("D) Helping people and making an impact")
    ans=input("enter your option").lower()
    if ans!= 'a' and ans!='b' and ans!='c' and ans!='d':
        print("INVALID OPTION")
    return ans
result4=four()
print(result4)


print("\n----- END OF QUESTIONS -----")
print("PERSONALITY : GREAT ")