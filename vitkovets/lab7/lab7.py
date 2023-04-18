import string
import random

# генеруємо рядок з 25 випадкових букв
random_string = ''.join(random.sample(string.ascii_letters, k=25))

# записуємо рядок у файл
with open('random_string.txt', 'w') as f:
    f.write(random_string)

