menuList = []
priceList = []


def showBill():
    print("---- My Food----")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        total += float(priceList[number])

    print("total = ",total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()


