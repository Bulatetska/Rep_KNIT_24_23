import string
import random
import json
import datetime
random_string = ''.join(random.choices(string.ascii_lowercase, k=25))
with open('random_string.txt', 'w') as f:
    f.write(random_string)
users = ["Артур", "Кейт", "Аліса", "Майк"]
users_data = []

for user in users:
    user_data = {}
    user_data["name"] = user
    user_data["age"] = random.randint(1, 99)
    users_data.append(user_data)

final_data = {}
final_data["data"] = users_data
final_data["created_at"] = datetime.datetime.now().strftime("%d;%m;%y")

filename = "users_data_" + final_data["created_at"] + ".json"
with open(filename, "w") as file:
    json.dump(final_data, file, ensure_ascii=False, indent=4)

print("Файл", filename, "успішно збережено")
