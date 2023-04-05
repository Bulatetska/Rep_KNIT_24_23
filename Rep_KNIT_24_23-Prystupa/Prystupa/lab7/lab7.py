import string
import random

random_string = ''.join(random.choice(string.ascii_letters) for i in range(25))
with open('random_string.txt', 'w') as file:
    file.write(random_string)

    import json
    import datetime
    import random

    users = ["Артур", "Кейт", "Аліса", "Майк"]
    users_data = []

    for user in users:
        user_data = {"name": user, "age": random.randint(1, 99)}
        users_data.append(user_data)

    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    final_dict = {"data": users_data, "created_at": current_date}

    with open(f"users_data_{current_date}.json", "w") as file:
        json.dump(final_dict, file)