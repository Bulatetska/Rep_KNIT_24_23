class Car:
    def __init__(self, brand, color, engineVolume):
        self.brand = brand
        self.color = color
        self.engineVolume = engineVolume

    def goForward(self):
        print(f"The {self.color} {self.brand} car is going forward.")

    def goBackward(self):
        print(f"The {self.color} {self.brand} car is going backward.\n")


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


car1 = Car("BMW", "black", 4.5)
car1.goForward()
car1.goBackward()

car2 = CarWithTurning("Audi", "white", 5.0)
car2.turnLeft()
car2.turnRight()

airplane = Airplane("BSC")
airplane.takeOff()

flyingCar = FlyingCar("Mercedes", "green", 6.0, "BLC")
flyingCar.goBackward()
flyingCar.takeOff()
