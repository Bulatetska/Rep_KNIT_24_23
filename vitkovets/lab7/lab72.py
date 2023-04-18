import json
import random
import string
from datetime import datetime

users = ["Артур", "Кейт", "Аліса", "Майк"]

l = []
for user in users:
    data = {
        "name": user,
        "age": random.randint(1, 99)
    }
    l.append(data)

cur_date = datetime.now().strftime("%d;%m;%y")

f_data = {
    "data": l,
    "created_at": cur_date
}

with open(f'users_data_{cur_date}.json', 'w') as file:
    json.dump(f_data, file)