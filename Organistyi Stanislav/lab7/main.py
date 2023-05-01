import json
import random
import string
from datetime import datetime
randstring = ''.join(random.choices(string.ascii_lowercase, k = 25))
with open('randstring.txt', 'w') as f:
    f.write(randstring)

users = ["Arthur", "Kate", "Alice", "Mike"]

    users_list = []
    for user in users:
        user_data = {
            "name": user,
            "age": random.randint(1, 99)
        }
        users_list.append(user_data)

    current_date = datetime.now().strftime("%d;%m;%y")

    final_data = {
        "data": users_list,
        "created_at": current_date
    }

    with open(f'users_data_{current_date}.json', 'w') as file:
        json.dump(final_data, file)