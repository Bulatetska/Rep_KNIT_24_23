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


# Створення об'єкту класу Car
my_car = Car('Audi', 'black', 2.0)
my_car1 = CarWithTurning('BMW', 'blue', 3.0)
# Виклик методів класу Car
my_car.drive_forward()
my_car.drive_backward()
my_car1.turn_left()
my_car1.turn_right()