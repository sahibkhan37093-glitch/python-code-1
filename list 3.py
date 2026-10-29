menu =["samosa","chai","burger","pizza","cold drink","coffee"]
print("starting menu:", menu)
menu.append("momos")
print(menu)
menu.insert(2,"pasta")
print(menu)
menu.remove("chai")
print(menu)
menu.pop()
menu.sort()
print(menu)
menu.reverse()
print(menu)
print(len(menu))
print(menu)
for i in range(len(menu)):
    print(f"{i+1}.{menu[i]}")
print(menu[0:3])
item= input("what item you should need") 
if item in menu:
    print("find item")  
else:
    print("not find")    

