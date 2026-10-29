bill = 0
print("menu:samosa-20,chait-15,burger-50")
order = input("what to order")
if order == "samosa":
    bill = 20
elif order == "chai":
    bill = 15
elif order =="burger":
    bill = 40
else:
    print("item not found") 
if bill > 0:
    print("your bill is") 
paisa = int(input("how much money you give me"))  
if paisa >= bill:
    print("take your chance")
    print("thanks come again")
else:
    print("pay some more bill the money is less than your order")    



