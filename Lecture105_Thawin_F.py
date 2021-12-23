class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditionner(self):
        print("Turn On : Air")

class Car(Vehicle):
    def nameCar(self):
        print("Car1")
class Pickup(Vehicle):
    def nameCar(self):
        print("Pickup1")
class Van(Vehicle):
    def nameCar(self):
        print("Van1")
class Estatecar(Vehicle):
    def nameCar(self):
        print("EstateCar1")

car1 = Car()
car1.nameCar()
car1.turnOnAirConditionner()

pickup1 = Pickup()
pickup1.nameCar()
pickup1.turnOnAirConditionner()

van1 = Van()
van1.nameCar()
van1.turnOnAirConditionner()

estate1 = Estatecar()
estate1.nameCar()
estate1.turnOnAirConditionner()