class Car:
    def __init__(self, brand, color, engine_size):
        self.brand = brand
        self.color = color
        self.engine_size = engine_size
    def drive_forward(self):
        print("Drive forward")
    def drive_backward(self):
        print("Drive backward")
class Car2(Car):
    def turn_left(self):
        print("Turn left")
    def turn_right(self):
        print("Turn right")
class Airplane:
    def __init__(self, model):
        self.model = model
    def take_off(self):
        print("Take off")
class FlyingCar(Car2, Airplane):
    def __init__(self, brand, color, engine_size, model):
        Car2.__init__(self, brand, color, engine_size)
        Airplane.__init__(self, model)

car = FlyingCar("Tesla", "red", 2.0, "FlyCar 3000")
car.drive_forward()
car.turn_left()
car.take_off()