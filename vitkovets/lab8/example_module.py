import math

def main(a, b, c):
    # Обчислюємо дискримінант
    discriminant = b**2 - 4*a*c
    
    # Якщо дискримінант менший за нуль, коренів немає
    if discriminant < 0:
        return None, None
    
    # Якщо дискримінант дорівнює нулю, є один корінь
    elif discriminant == 0:
        x = -b / (2*a)
        return x, None
    
    # Якщо дискримінант більше нуля, є два корені
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
