from example_module import main

a = 2
b = -5
c = 6

x1, x2 = main(a, b, c)

if x1 is not None:
    print(f"Рівняння має корені: x1 = {x1}, x2 = {x2}")
else:
    print("Рівняння не має дійсних коренів")