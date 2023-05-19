import string
import random
import json

random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(25))

with open('D://Study//2 course(II)//Програмування Python//Rep_KNIT_24_23//Omelianchuk '
          'Volodymyr//lab_6//random_string.txt', 'w') as file:
    file.write(random_string)

    from datetime import datetime

users = ["Артур", "Кейт", "Аліса", "Майк"]

users_data = []

for user in users:
    user_data = {"name": user, "age": random.randint(1, 99)}
    users_data.append(user_data)

final_dict = {"data": users_data, "created_at": datetime.now().strftime("%d;%m;%y")}

with open(f'users_data_{final_dict["created_at"]}.json', 'w') as f:
    json.dump(final_dict, f, ensure_ascii=False)
