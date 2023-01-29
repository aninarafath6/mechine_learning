# inheritance

class Vehicle:
    color = "red"
    speed = "100km/h"
    mileage = "50km"

    def __init__(self, color):
        self.color = color


class Car(Vehicle):
    pass

    def displayCar(self):
        print("color: ", self.color)


swift = Car("blue")
swift.displayCar()
