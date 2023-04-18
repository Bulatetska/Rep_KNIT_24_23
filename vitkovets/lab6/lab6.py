class Car:
    def __init__(self, brand, color, engine_size):
        self.brand = brand
        self.color = color
        self.engine_size = engine_size
    
    def drive_forward(self):
        print(f"The {self.color} {self.brand} is driving forward.")
    
    def drive_backward(self):
        print(f"The {self.color} {self.brand} is driving backward.")
    
    def turn_left(self):
        print(f"The {self.color} {self.brand} is turning left.")
    
    def turn_right(self):
        print(f"The {self.color} {self.brand} is turning right.")

class Turning(Car):
    def turn_left(self):
        print(f"The {self.color} {self.brand} is turning left.")
    
    def turn_right(self):
        print(f"The {self.color} {self.brand} is turning right.")

class Airplane:
    def __init__(self, model):
        self.model = model
    
    def take_off(self):
        print(f"The {self.model} airplane is taking off.")

class CarAirplane(Turning, Airplane):
    def __init__(self, brand, color, engine_size, model):
        Car.__init__(self, brand, color, engine_size)
        Airplane.__init__(self, model)

mycar_airplane = CarAirplane("Toyota", "Black", "2.0L", "Cessna 172")
mycar_airplane.drive_forward()
mycar_airplane.turn_left()
mycar_airplane.take_off()


