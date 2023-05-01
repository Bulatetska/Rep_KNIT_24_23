class Car:
    def __init__(self, mark, color, engine_size):
        self.brand = mark
        self.color = color
        self.engine_size = engine_size

    def forward(self):
        print(self.color, self.brand, "Moving forward")

    def backward(self):
        print(self.color, self.brand, "Moving backward")


Car1 = Car("Porsche", "Black", '3.2')

Car1.forward()
Car1.backward()


class Car2(Car):
    def left(self):
        print(self.color, self.brand, "Moving left")

    def right(self):
        print(self.color, self.brand, "Moving right")


с2 = Car2("Ferrari", "Green", '3.1')

с2.forward()
с2.backward()
с2.left()
с2.right()


class Plane:
    def __init__(self, model):
        self.model = model

    def fly(self):
        print(self.model, "Takes off")


a1 = Plane("MRI9")
a1.fly()


class Car2_Plane(Car2, Plane):
    def __init__(self, mark, color, engine_size, model):
        Car2.__init__(self, mark, color, engine_size)
        Plane.__init__(self, model)


ac1 = Car2_Plane("Ford", "White", "3.3)", "Urus")

ac1.forward()
ac1.backward()
ac1.left()
ac1.right()
ac1.fly()