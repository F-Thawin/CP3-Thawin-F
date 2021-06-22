menuList = []
priceList = []

def showBill():
    print("myFood".center(16,"-"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
    print("ราคาทั้งหมด:",sum(priceList),"THB")

while True:
    menuName = input("Please Enter Menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)
showBill()

