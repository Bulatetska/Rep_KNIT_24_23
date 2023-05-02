import string
import random

# створюємо рядок з усіма буквами англійського алфавіту
alphabet = string.ascii_lowercase

# генеруємо рядок з 25 випадкових символів з алфавіту
random_string = ''.join(random.choice(alphabet) for i in range(25))

# записуємо рядок у файл
with open('random_string.txt', 'w') as f:
    f.write(random_string)
