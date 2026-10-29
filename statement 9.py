people_percentage = int(input("enter percentage of people"))
students = int(input("how many % peoples are students "))
country = input("enter your country")
if students == 10:
    print("country is in less education system")
elif students == 40:
    print("country is a littel good in education system")    
elif students >= 50 and students <= 80:
    if country =="india":
        print("education system is super")
    else:
        print("normal education system")   
else:
    print("normal education")  
