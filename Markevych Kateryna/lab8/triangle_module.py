def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_triangle_area_by_sides(side1, side2, side3):
    # Перевірка на тип трикутника
    if side1 == side2 == side3:
        # Рівносторонній трикутник
        return (side1 ** 2 * 3 ** 0.5) / 4
    elif side1 == side2 or side2 == side3 or side1 == side3:
        # Рівнобедрений трикутник
        semi_perimeter = (side1 + side2 + side3) / 2
        return (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5
    else:
        # Звичайний трикутник
        semi_perimeter = (side1 + side2 + side3) / 2
        return (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5
