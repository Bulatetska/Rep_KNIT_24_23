print("#TASK 1")
class Car:
    def __init__(self, brand, color, engine_size):
        self.brand = brand
        self.color = color
        self.engine_size = engine_size
    
    def drive_forward(self):
        print("Drive forward")
    
    def drive_backward(self):
        print("Drive backward")

carInstance = Car("Ford", "Gray", '4.5')

print(f'Car - Brand: {carInstance.brand}, Color: {carInstance.color}, Engine size: {carInstance.engine_size}')
carInstance.drive_forward()
carInstance.drive_backward()



print("\n#TASK 2")
class Car2(Car):
    def turn_left(self):
        print("Turn left")
    
    def turn_right(self):
        print("Turn right")

carInstance2 = Car2("Toyota", "Black", '4')

print(f'Car2 - Brand: {carInstance2.brand}, Color: {carInstance2.color}, Engine size: {carInstance2.engine_size}')

carInstance2.drive_forward()
carInstance2.drive_backward()
carInstance2.turn_left()
carInstance2.turn_right()



print("\n#TASK 3")
class Airplane:
    def __init__(self, model):
        self.model = model
    
    def take_off(self):
        print("Take off")


airInstance = Airplane('Boeing')

print(f'Airplane - Model: {airInstance.model}')
airInstance.take_off()

print("\n#TASK 4")
class FlyingCar(Car2, Airplane):
   def __init__(self, brand, color, engine_size, model):
        Car2.__init__(self, brand, color, engine_size)
        Airplane.__init__(self, model)

flyingCarInstance = FlyingCar("DeLorean", "Silver", "2.8", "Boeing 737")


print(f'FlyingCar - Brand: {flyingCarInstance.brand}, Color: {flyingCarInstance.color}, Engine size: {flyingCarInstance.engine_size}, Model: {flyingCarInstance.model}')
flyingCarInstance.drive_forward()
flyingCarInstance.drive_backward()
flyingCarInstance.turn_left()
flyingCarInstance.turn_right()
flyingCarInstance.take_off()
