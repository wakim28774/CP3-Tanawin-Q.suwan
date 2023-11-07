num = int(input("Enter number: "))

for x in range(num):
    text = " " * ( num - x - 1)
    for y in range(x * 2 + 1):
        text += "*"
    print(text)