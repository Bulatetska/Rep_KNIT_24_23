import math
import random
import datetime

year = random.randint(1940, 2022)
month = random.randint(1, 12)
day = random.randint(1, 28)
random_date = datetime.date(year, month, day)

today = datetime.date.today()
delta = today - random_date
days_difference = abs(delta.days)

factorial = math.factorial(8)

print("Випадкова дата:", random_date.strftime("%d-%m-%Y"))
print("Різниця між випадковою та сьогоднішньою датою:", days_difference, "днів")
print("Факторіал числа 8:", factorial)