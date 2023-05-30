# Модуль distance
def calculate_distance(origin, destination):
    # Код для обчислення відстані між початковим і кінцевим місцями розташування
    # Цей код можна виконати шляхом використання API картографії або бази даних
    distance = 100  # Приклад відстані (замініть це реальним обчисленням)
    return distance

# Модуль fuel
def calculate_fuel_cost(distance, fuel_price_per_liter, fuel_efficiency):
    fuel_consumption = distance / fuel_efficiency
    fuel_cost = fuel_consumption * fuel_price_per_liter
    return fuel_cost

# Модуль accommodation
def calculate_accommodation_cost(nights, price_per_night):
    accommodation_cost = nights * price_per_night
    return accommodation_cost

# Основний модуль
def calculate_total_trip_cost(origin, destination, fuel_price_per_liter, fuel_efficiency, nights, price_per_night):
    distance = calculate_distance(origin, destination)
    fuel_cost = calculate_fuel_cost(distance, fuel_price_per_liter, fuel_efficiency)
    accommodation_cost = calculate_accommodation_cost(nights, price_per_night)
    total_cost = fuel_cost + accommodation_cost
    return total_cost

# Приклад використання
origin = "Місто А"
destination = "Місто Б"
fuel_price_per_liter = 5.6
fuel_efficiency = 10
nights = 3
price_per_night = 100

total_trip_cost = calculate_total_trip_cost(origin, destination, fuel_price_per_liter, fuel_efficiency, nights, price_per_night)
print("Загальна вартість подорожі:", total_trip_cost)