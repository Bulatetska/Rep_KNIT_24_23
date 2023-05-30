import triangle_module

# Розрахунок площі трикутника за висотою та основою
base = 6
height = 4
area = triangle_module.calculate_triangle_area(base, height)
print(f"The area of the triangle with base {base} and height {height} is {area}.")

# Розрахунок площі трикутника за довжинами сторін
side1 = 3
side2 = 4
side3 = 5
area = triangle_module.calculate_triangle_area_by_sides(side1, side2, side3)
print(f"The area of the triangle with sides {side1}, {side2}, {side3} is {area}.")
