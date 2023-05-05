import random
import string

# Генеруємо рядок з 25 випадкових букв англійського алфавіту
random_string = ''.join(random.choices(string.ascii_letters, k=25))

# Записуємо рядок у файл
with open('random_string.txt', 'w') as f:
    f.write(random_string)
