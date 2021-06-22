systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันไก่ทอด":45,"ข้าวหมูแดง":50}
menuList = []
def showBill():
    total = 0
    print("myFood".center(16,"-"))
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total += menuList[number][1]
    print("ราคาทั้งหมด:",total,"THB")

while True:
    menuName = input("Please Enter Menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
        print(menuList)
print(menuList)
showBill()

