import string
import random
import json

random_string = 'Ukraine is the best count' #створюємо рядок з 25-ти символів

f = open('random_string.txt', 'w') #відкриваємо файл random_string.txt

f.write(random_string) #записуємо рядок у файл

from datetime import datetime #використовуємо бібліотеку дати

users = ["Артур", "Кейт", "Аліса", "Майк"] #створюємо масив користувачів

users_data = [] #створюємо масив для даних про користувачів

for user in users:
    user_data = {"name": user, "age": random.randint(1, 99)} #створюємо словник із іменами користувачів та рандомним віком
    users_data.append(user_data) #додаємо до масиву

final_dict = {"data": users_data, "created_at": datetime.now().strftime("%d;%m;%y")} #створюємо словник назви файлу з поточною датою

with open(f'users_data_{final_dict["created_at"]}.json', 'w') as f: #створюємо файл json
    json.dump(final_dict, f, ensure_ascii=False)
