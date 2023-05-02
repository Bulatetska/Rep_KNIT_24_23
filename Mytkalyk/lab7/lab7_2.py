import datetime
import json
import random

# список користувачів
users = ["Daniel", "Alina", "Vova", "Vadym", "Sasha"]

# створюємо список словників з випадковим віком
user_data = []
for user in users:
    user_dict = {}
    user_dict["name"] = user
    user_dict["age"] = random.randint(1, 99)
    user_data.append(user_dict)

# створюємо словник з поточною датою та списком словників з користувачами
now = datetime.datetime.now()
data = {}
data["created_at"] = now.strftime("%d;%m;%y")
data["data"] = user_data

# записуємо словник у json файл
filename = f"users_data_{now.strftime('%Y-%m-%d')}.json"
with open(filename, "w") as f:
    json.dump(data, f)
