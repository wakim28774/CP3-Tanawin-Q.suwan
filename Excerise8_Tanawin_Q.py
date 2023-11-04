username = input("Username : ")
password = input("Password : ")
if username == "Wakim" and password == "0000" :
    print("Welcome to restaurant !")
    print("This is the menu you can order.")
    print("1.tomato 50 THB")
    print("2.mile    20 THB")
    print("3.tea  60 THB")
    print("4.Water         10 THB")
    SelectMenu = int(input("Please select menu. >> "))
    Amount = int(input("How many do you want? >> "))
    if SelectMenu == 1:
        print("Total Payment : ",50*Amount,"THB")
    elif SelectMenu == 2:
        print("Total Payment : ",20*Amount,"THB")
    elif SelectMenu == 3:
        print("Total Payment : ",60*Amount,"THB")
    elif SelectMenu == 4:
        print("Total Payment : ",10*Amount,"THB")
    else:
        print("Invalid number of menu.")
    print("Thank you for using the service.")
else:
    print("Invaild Username or Password.")