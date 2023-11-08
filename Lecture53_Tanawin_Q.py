def vatCalculate(price):
    result = price+(price*7/100)
    return result

price = float(input("Enter price: "))

totalWithVat = vatCalculate(price)

print("Price with VAT:", totalWithVat)