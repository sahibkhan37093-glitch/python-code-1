marks = int(input("enter your marks"))
attendance = int(input("enter your attendance"))
assignment = input("yes/no")
fees = input("paid/unpaid")
if fees == "unpaid":
    print("result blocked- pay fees")
elif fees== "paid":
    if attendance <= 50:
        print("fail - short attendance") 
    elif attendance >= 50 and attendance <= 100:
        if marks <= 33:
            print("fail- less marks")  
        elif marks >= 33 and marks <= 59:
            if assignment == "yes":
                print("pass- grade D")
            else:
                print("pass- grade D but assignment pending") 
        elif marks >= 60 and marks <= 79:
            if assignment == "yes":
                print("pass- grade B")
            else:
                print("pass- assignment miss")    
        elif marks >= 80 and marks <= 100:
            if attendance == "90"        :
                print("pass- grade A+ honours")
            else:
                print("pass - grade A")    

