class Car:
    def __init__(self, brand, color, engine_size):
        self.brand = brand
        self.color = color
        self.engine_size = engine_size

    def drive_forward(self):
        print("Drive forward")

    def drive_backward(self):
        print("Drive backward")


class TurnCar(Car):
    def turn_left(self):
        print("Turn left")

    def turn_right(self):
        print("Turn right")


class Airplane:
    def __init__(self, model):
        self.model = model

    def take_off(self):
        print("Take off")


class FlyingCar(TurnCar, Airplane):
    def __init__(self, brand, color, engine_size, airplane_model):
        Car.__init__(self, brand, color, engine_size)
        Airplane.__init__(self, airplane_model)


def main():
    data_choice = input("Do you want to use pre-filled data? (y/n): ")
    if data_choice.lower() == "y":
        my_car = Car("Toyota", "red", 2.5)
        my_airplane = Airplane("Cessna")
    else:
        brand = input("Enter the car brand: ")
        color = input("Enter the car color: ")
        engine_size = float(input("Enter the car engine size: "))
        airplane_model = input("Enter the airplane model: ")
        my_car = Car(brand, color, engine_size)
        my_airplane = Airplane(airplane_model)

    print("Car brand:", my_car.brand)
    print("Car color:", my_car.color)
    print("Car engine size:", my_car.engine_size)
    my_car.drive_forward()  # Output: Drive forward
    my_car.drive_backward()  # Output: Drive backward

    print("Airplane model:", my_airplane.model)
    my_airplane.take_off()
    my_flying_car = FlyingCar(my_car.brand, my_car.color, my_car.engine_size, my_airplane.model)
    print("Flying car brand:", my_flying_car.brand)
    print("Flying car color:", my_flying_car.color)
    print("Flying car engine size:", my_flying_car.engine_size)
    print("Flying car model:", my_flying_car.model)
    my_flying_car.turn_left()  # Output: Turn left
    my_flying_car.turn_right()  # Output: Turn right
    my_flying_car.take_off()  # Output: Take off


if __name__ == "__main__":
    main()
