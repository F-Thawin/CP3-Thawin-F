username = input(str("Username: "))
password = input(str("Password: "))
if username == "F.thawin" and password == "james12345":
    print("Welcome to Fruity Shop")
    print("----List of Procduct----")
    print("1.Apple : 20THB/PCS")
    print("2.Banana : 10THB/PCS")
    print("3.Pineapple : 20THB/PCS")
    apple = 20
    totalApple = 0
    banana = 10
    totalBanana = 0
    pineapple = 20
    totalPineapple = 0
    fruit = input("Select Product (If your want to exit press E):")
    if fruit == "1":
        pieces = int(input("How many pieces?: "))
        totalApple = apple*pieces
        print("Your apple price is ",totalApple,"THB")
        print("Thank you")
    elif fruit == "2":
        pieces = int(input("How many pieces?: "))
        totalBanana = banana * pieces
        print("Your Banana price is ",totalBanana,"THB")
        print("Thank you")
    elif fruit == "3":
        pieces = int(input("How many pieces?: "))
        totalPineapple = pineapple * pieces
        print("Your Pineapple price is ",totalPineapple,"THB")
        print("Thank you")
    else:
        print("Good bye!")
else:
    print("Login false!")
