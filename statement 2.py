age = int(input("enter your age"))   
student= input("yes/no")
distance = int(input("enter distance"))
days = int(input("how much days pass u have to need_30/90/365"))
if distance <= 5:
    print("no pass needed")
elif distance >= 5 and distance <= 20:
    if student == "yes":
        if days == 365:
            print("student yearly-2000 Rs")
        else:
            print("student monthly- 200 Rs")    
    elif student == "no":
        if days == 30:
            print("normal monthly- 400")  
        else:
            print("normal 3 month- 1000Rs")     
if distance>= 20:
    if age >= 60:
        print("senior pass-300 Rs(same for all days)")    
    else:
        if days == 365:
            print("long yearly- 5000 Rs")  
        else:
            print("long monthly- 800 Rs")                  


        
