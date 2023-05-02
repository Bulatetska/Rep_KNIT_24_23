import string
import random

random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(25))

with open('random_string.txt', 'w') as file:
    file.write(random_string)
