marks = int(input("enter marks"))
attendance = int(input("give attendance %"))
Name = input("enter you name")
Roll = int(input("enter your roll no"))
class_name = input("enter your class")
print(marks)
print(attendance)
print(Name)
print(Roll)
print(class_name)
if attendance < 75:
    print("fail: attendance is less")
else:
    if marks >= 90:
        print("grade A+|Scholarsgip: 100% ")  
    elif marks >= 75:
        print("grade A |Scholarship: 50%")
    elif marks >= 60:
        if attendance >= 90:
            print("grade B|attendace good 20% scholarship")
        else:
            print("gradeB|no scholarship")      
    elif marks >= 33:
        print("grade c|only pass")    
    else:
        print("fail:marks are less") 
