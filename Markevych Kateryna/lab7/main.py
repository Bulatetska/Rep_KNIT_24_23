import string
import random
import json
from datetime import datetime
from random import randint
print('1.')
random_string = ''.join(random.choice(string.ascii_letters) for i in range(25))
with open('my_folder/random_string.txt', 'w') as file:
    file.write(random_string)
    print(random_string)
print('2.')
users = ["Артур", "Кейт", "Аліса", "Майк"]
users_data  = []
for user in users:
    user_data = {"name: ": user, "age: ": randint(1,99)}
    users_data.append(user_data)
data = {"data":user_data, "created_at":datetime.now().strftime("%d;%m;%Y")}
filename = f"my_folder/users_data_{datetime.now().strftime('%d-%m-%Y')}.json"
with open(filename, "w") as file:
    json.dump(data, file, ensure_ascii=False)
    print(users_data)