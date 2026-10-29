def bank_account():
    name = input("enter your name")
    choice = input("open bank account(a/b)")
    if choice == "a":
        account = input("enter your account ")
    else:
        account = "saving account"   
    return name, account
result = bank_account()     
print(result)
