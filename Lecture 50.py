def addNumber(x,y,z):
    if z == "+":
        print(x+y)
    elif z == "-":
        print(x-y)
    elif z == "*":
        print(x*y)
    elif z == "/":
        print(x/y)
addNumber(int(input("input x: ")),int(input("input y: ")),input("Should calculation(+,-,*,/): "))