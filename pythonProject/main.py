import random
import string

red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)
random_color = (red, green, blue)

print(random_color)

random_food_char = random.choice(string.ascii_uppercase)

print(random_food_char)
