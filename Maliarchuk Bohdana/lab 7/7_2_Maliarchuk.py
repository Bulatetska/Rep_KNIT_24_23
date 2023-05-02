import json
import datetime
import random

users = ["Артур", "Кейт", "Аліса", "Майк"]
user_data = []

for name in users:
    user_data.append({"name": name, "age": random.randint(1, 99)})

current_date = datetime.datetime.now().strftime("%d;%m;%y")
data = {"data": user_data, "created_at": current_date}

filename = f"users_data_{current_date}.json"
with open(filename, "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Файл {filename} успішно створено!")
