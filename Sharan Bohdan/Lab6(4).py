class Car:
    def __init__(self, brand, color, engine_size):
        self.brand = brand
        self.color = color
        self.engine_size = engine_size

    def drive_forward(self):
        print(f"The {self.color} {self.brand} is driving forward")

    def drive_backward(self):
        print(f"The {self.color} {self.brand} is driving backward")

class CarWithTurning(Car):
    def __init__(self, brand, color, engine_size):
        super().__init__(brand, color, engine_size)
        self.direction = "straight"

    def turn_left(self):
        print(f"The {self.color} {self.brand} is turning left")
        self.direction = "left"

    def turn_right(self):
        print(f"The {self.color} {self.brand} is turning right")
        self.direction = "right"

class Airplane:
    def __init__(self, model):
        self.model = model

    def takeoff(self):
        print(f"The {self.model} is taking off")
class FlyingCar(CarWithTurning, Airplane):
    def __init__(self, brand, color, engine_size, model):
        CarWithTurning.__init__(self, brand, color, engine_size)
        Airplane.__init__(self, model)

    def fly(self):
        if self.direction == "straight":
            print(f"The {self.color} {self.brand} is flying {self.direction} and {self.model} is flying straight")
        else:
            print(f"The {self.color} {self.brand} is flying {self.direction} and {self.model} is unable to fly in that direction")


# Створення об'єкту класу Carplane
my_carplane = FlyingCar('Tesla', 'red', 3.0, 'Boeing 747')

# Виклик методів класів Car та Airplane через успадкування
my_carplane.drive_forward()
my_carplane.drive_backward()
my_carplane.turn_left()
my_carplane.turn_right()
my_carplane.takeoff()