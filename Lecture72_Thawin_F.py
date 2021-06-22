menuList = []
def showBill():
    total = 0
    print("myFood".center(16,"-"))
    for number in range(len(menuList)):
        print(menuList[number][0])
        total += menuList[number][1]
    print("ราคาทั้งหมด:",total,"THB")

while True:
    menuName = input("Please Enter Menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()

