class Car:
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume
        print(self.color, self.brand, self.volume)

    def drive_forward(self):
        print("Їду вперед")

    def drive_backward(self):
        print("Їду назад")


class CarII(Car):
    def turn_left(self):
        print("Рухаюсь ліворуч")

    def turn_right(self):
        print("Рухаюсь праворуч")


class Airplane:
    def __init__(self, model):
        self.model = model

    def take_off(self):
        print("ЗЛІТАЮ")
class Car_plus_Airplane(CarII, Airplane):
    pass

Audi = Car('Herman', 'black', '100')
Audi.drive_backward()
Audi.color = 'Blue'
print(Audi.color)
Sky = Car_plus_Airplane('dream', 'red', '100')
Sky.take_off()
print(Sky.color)