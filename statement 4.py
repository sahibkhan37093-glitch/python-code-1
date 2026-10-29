book_days= int(input("how days you take book "))
student_type = input("give student type(regular/top):")
damage = input("book damagrd or not (yes/no):")
if book_days <=7:
    print("no fine - return on time")
elif  book_days <= 15:
    if student_type-type == "top":
        print("fine: 10Rs only- top student discount")
    else:
        print("fine: 15 Rs")    
elif book_days <= 30:
    if damage == "yes":
        print("fine:200 Rs+damage charge 100 Rs = 300 Rs")
    else:
        print("fine:200 Rs")    
else:
    if damage == "yes" :
        print("membership canel+ 500 Rs fine")  
    else:
        print("membership warning + 300 Rs fine")  
