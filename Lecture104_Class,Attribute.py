class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Thawin"
customer1.lastName = "Fufuangvanich"
customer1.addCart()

customer2 = Customer()
customer2.name = "Kullanut"
customer2.lastName = "Wongyos"
customer2.addCart()

customer3 = Customer()
customer3.name = "Tawankhun"
customer3.lastName = "Kittinutthapong"
customer3.addCart()

customer4 = Customer()
customer4.name = "Supansa"
customer4.lastName = "Ritthimarn"
customer4.addCart()