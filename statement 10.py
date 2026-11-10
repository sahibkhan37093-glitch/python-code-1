name = input("enteryour name")
job = input("enteryour job")
company = input("enter your company")
salary = int(input("enter you salary"))
print(name)
print(job)
print(company)
print(salary)
if salary == 10000:
    print("bad job")
elif salary > 10000 and salary <= 50000:
    if salary == 20000:
        if job == "manager":
            print("less salary , good personality")
        else:
            print("less personality as well as less salary")   
    elif salary == 40000:
        if job == "engineer":
            print("good job and good salary")
        else:
            print("good job and normal salary")
else:
    print("superb",name,job,company)                     
