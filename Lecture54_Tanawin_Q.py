def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        print(" username or password incorrect, please try again.")
        login()
def showMenu():
    print("----- TWShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print(vatCaculate(float(input("Price (THB) : "))))
    elif userSelected == 2:
        print(priceCalculate())
def vatCaculate(totalPrice):
    vat = 7
    return totalPrice + (totalPrice * vat / 100)
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1+price2
    return vatCaculate(totalPrice)

print(login())