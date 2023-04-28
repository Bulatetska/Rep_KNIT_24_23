class Airplane:
    def __init__(self, model):
        self.model = model

    def takeoff(self):
        print(f"The {self.model} is taking off")

# Створення об'єкту класу Airplane
my_plane = Airplane('Boeing 747')

# Виклик методу класу Airplane
my_plane.takeoff()