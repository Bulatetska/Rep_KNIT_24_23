import string
import random
import time
import json

# Randomly choose a letter from all the ascii_letters

f1 = open("random_string.txt", 'wt')

i = 0
while i < 25:
    randLetter = random.choice(string.ascii_letters)
    f1.write(randLetter + " ")
    i += 1
f1.close()

#TASK 2
listUsers = [{'name': "Артур", 'age': 22},{'name': "Кейт", 'age': 25},{'name': "Аліса", 'age': 19},{'name': "Майк", 'age': 35}]

now = time.strftime("%d-%m-%y", time.localtime())

mainDict = {'data': listUsers, 'created_at': now}

path = 'users_data_{}.json'.format(now)

with open(path, 'w') as file:
    json.dump(mainDict, file, indent=4)
