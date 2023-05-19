import math


class Car:
    def __init__(self, brand, color, engineVolume, amount_places):
        self.brand = brand
        self.color = color
        self.engineVolume = engineVolume
        self.amount_places = amount_places

    def goForward(self):
        print(f"The {self.color} {self.brand} car is going forward.")

    def goBackward(self):
        print(f"The {self.color} {self.brand} car is going backward.\n")

    def transportation(self, people):
        return math.ceil(people / (self.amount_places - 1))

    def print_transportation(self, people):
        driving = Car.transportation(self, people)
        print(f"Потрібно {driving} поїздок для перевезення {people} людей")


class CarWithTurning(Car):
    def turnLeft(self):
        print(f"The {self.color} {self.brand} car is turning left.")

    def turnRight(self):
        print(f"The {self.color} {self.brand} car is turning right.\n")


class Airplane:
    def __init__(self, model):
        self.model = model

    def takeOff(self):
        print(f"The {self.model} airplane is taking off.\n")


class FlyingCar(CarWithTurning, Airplane):
    def __init__(self, brand, color, engineVolume, model):
        Car.__init__(self, brand, color, engineVolume)
        Airplane.__init__(self, model)


car1 = Car("BMW", "black", 4.5, 5)
car1.print_transportation(18)
