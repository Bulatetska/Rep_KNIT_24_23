from Models.CountdownTile import CountdownTile
import random
import string

class FoodTile(CountdownTile):
    def __init__(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        random_color = (red, green, blue)

        random_food_char = random.choice(string.ascii_uppercase)
        super().__init__(random_color, random_food_char, 10)
    
    def onCountdownEnd(self):
        self.delete()

    