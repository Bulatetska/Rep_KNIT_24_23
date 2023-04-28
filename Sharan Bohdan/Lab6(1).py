class Car:
    def __init__(self, brand, color, engine_size):
        self.brand = brand
        self.color = color
        self.engine_size = engine_size

    def drive_forward(self):
        print(f"The {self.color} {self.brand} is driving forward")

    def drive_backward(self):
        print(f"The {self.color} {self.brand} is driving backward")


# Створення об'єкту класу Car
my_car = Car('Audi', 'black', 2.0)

# Виклик методів класу Car
my_car.drive_forward()
my_car.drive_backward()