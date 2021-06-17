def addNumber(x,y,z):
    if z == "+":
        print(x+y)
    elif z == "-":
        print(x-y)
    elif z == "*":
        print(x*y)
    elif z == "/":
        print(x/y)
addNumber(int(input("input number: ")),int(input("input number: ")),input("Should calculation(+,-,*,/): "))