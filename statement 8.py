income = int(input("enter your income"))
name = input("enter your name")
job = input("enter your job")
if income == 40000:
    print("i will think about this income")
elif income == 30000:
    if job == "good":
        print("i will do job")  
    else:
        print("not intrested")    
elif income >= 70000:
    print("good job")
else:
    print("i need a job")    
