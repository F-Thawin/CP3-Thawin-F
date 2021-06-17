def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Try again")
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("Price + Vat= ",vatCalculator())
    elif userSelected == 2:
        print("Price Non Vat= ",priceCalculator())
    else:
        return showMenu()
def vatCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    price3 = price1 + price2
    vat = 7
    result = price3 + (price3 * vat / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    result = price1 + price2
    return result
login()