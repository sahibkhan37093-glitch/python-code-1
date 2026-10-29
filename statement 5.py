amount = int(input("how much shopping you have done"))
member = input("gold/silver")
coupon = input("yes/no")
if amount <= 500:
    print("no discount")
elif amount >= 500 and amount <= 200:
    if member == "gold":
        print("20% discount")    
    else:
        print("10% discount")    
elif amount >= 2000:
    if coupon == "yes":
        print("30% + extra gift")
    elif coupon == "no":
        print("25% discount") 
else:
    print("no discount")        
