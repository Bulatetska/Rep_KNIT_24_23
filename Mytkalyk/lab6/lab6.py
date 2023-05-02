class Car:
    def __init__(self, brand, color, engine_capacity):
        self.brand = brand
        self.color = color
        self.engine_capacity = engine_capacity

    def drive_forward(self):
        print("Drive forward")

    def drive_backward(self):
        print("Drive backward")


class CarWithTurning(Car):
    def turn_left(self):
        print("Turn left")

    def turn_right(self):
        print("Turn right")


class Airplane:
    def __init__(self, model):
        self.model = model

    def take_off(self):
        print("Take off")


class FlyingCar(CarWithTurning, Airplane):
    def __init__(self, brand, color, engine_capacity, model):
        Car.__init__(self, brand, color, engine_capacity)
        Airplane.__init__(self, model)

    def fly(self):
        print("Flying")


#Car
my_car = Car("Mercedes", "white", "2.0L")
my_car.drive_forward()
my_car.drive_backward()

#CarWithTurning
my_car_with_turning = CarWithTurning("Audi", "black", "2.7L")
my_car_with_turning.drive_forward()
my_car_with_turning.turn_left()
my_car_with_turning.turn_right()

#Airplane
my_airplane = Airplane("Boeing 747")
my_airplane.take_off()

#FlyingCar
my_flying_car = FlyingCar("Tesla", "white", "electric", "Tesla-Plane")
my_flying_car.drive_forward()
my_flying_car.turn_left()
my_flying_car.take_off()
my_flying_car.fly()