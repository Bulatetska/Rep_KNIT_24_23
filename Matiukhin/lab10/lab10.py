import list_functions
import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

ls = [random.randint(0, 20) for i in range(10)]
print(ls)

print("------Avg------")
print(list_functions.avg(ls))

print("------Find Max------")
print(list_functions.find_top_5_max(ls))

print("------Find Min------")
print(list_functions.find_top_5_min(ls))

print("------Sort------")
print(list_functions.sort(ls, lambda a,b: is_prime(a)))

print("------Find Key------")
print(list_functions.find_key(ls, 7))

print("------Find Sequence------")
start = random.randint(0, len(ls) - 1)
finish = random.randint(start, len(ls) - 1)
seq = ls[start:finish]
print(seq)
print(list_functions.find_sequence(ls, seq))

print("------Get List Without Repetitions------")
print(list_functions.get_list_without_repetitions(ls))