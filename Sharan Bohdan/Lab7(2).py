import json
import datetime
import random

# Список користувачів
users = ["Артур", "Кейт", "Аліса", "Майк"]

# Створюємо список словників з випадковим віком для кожного користувача
users_list = [{"name": name, "age": random.randint(1, 99)} for name in users]

# Створюємо словник з даними та поточною датою
data_dict = {"data": users_list, "created_at": datetime.datetime.now().strftime("%d;%m;%y")}

# Записуємо словник у JSON-файл з ім'ям, що містить поточну дату
filename = f"users_data_{datetime.datetime.now().strftime('%Y-%m-%d')}.json"
with open(filename, "w") as f:
    json.dump(data_dict, f)
