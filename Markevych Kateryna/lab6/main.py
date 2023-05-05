class Car:
    def __init__(self, brand, color, engine_size):
        self.brand = brand
        self.color = color
        self.engine_size = engine_size

    def drive_forward(self):
        print("Driving forward")

    def drive_backward(self):
        print("Driving backward")
car1 = Car("Toyota", "Red", 2.0)
print("Car:")
print("brand:", car1.brand)
print("color:", car1.color)
print("engine", car1.engine_size)
car1.drive_forward()
print("")
class CarWithTurn(Car):
    def __init__(self, brand, color, engine_size):
        super().__init__(brand, color, engine_size)

    def turn_left(self):
        print("Turning left")

    def turn_right(self):
        print("Turning right")

car2 = CarWithTurn("Toyota", "Green", 3.0)
print("Car:")
print("brand:", car2.brand)
print("color:", car2.color)
print("engine", car2.engine_size)
car2.turn_right()
car2.drive_backward()
print("")
class Airplane:
    def __init__(self, model, hight):
        self.model = model
        self.hight = hight

    def takeoff(self):
        print("Taking off")

airplane1 = Airplane("Boeing 747",478)
airplane2 = Airplane("Boeing 747",478)
print("Airplane1 model and hight:", airplane1.model, airplane1.hight)
print("Airplane2 model and hight:", airplane2.model, airplane2.hight)
airplane1.takeoff()
if (airplane1.hight == airplane2.hight):
    print("Crack!")

print(" ")


class Flying_And_Car(CarWithTurn, Airplane):
    def __init__(self, brand, color, engine_size, model):
        CarWithTurn.__init__(self, brand, color, engine_size)
        Airplane.__init__(self, model)

    def fly(self):
        print("Flying")
flying_car1 = Flying_And_Car("Tesla", "Blue", 3.0, "Model S")
print("Brand:", flying_car1.brand)
print("Color:", flying_car1.color)
print("Engine Size:", flying_car1.engine_size)
print("Model:", flying_car1.model)
flying_car1.fly()
flying_car1.drive_forward()
flying_car1.turn_left()
flying_car1.takeoff()


