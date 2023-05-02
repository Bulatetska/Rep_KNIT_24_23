class Car:
    def __init__(self, brand, color, engine_volume):
        self.brand = brand
        self.color = color
        self.engine_volume = engine_volume

    def go_forward(self):
        print("The car is going forward")

    def go_backward(self):
        print("The car is going backward")

class TurnCar(Car):
    def turn_left(self):
        print("The car is turning left")

    def turn_right(self):
        print("The car is turning right")


car = TurnCar("Honda", "silver", 3.0)
car.go_forward() # виведе "The car is going forward"
car.turn_left() # виведе "The car is turning left"
car.turn_right() # виведе "The car is turning right"
