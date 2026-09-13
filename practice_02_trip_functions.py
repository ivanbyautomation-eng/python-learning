

def calculate_fuel(distance, fuel_consumption):
    return distance * fuel_consumption / 100


def calculate_cost(fuel_needed, price):
    return fuel_needed * price


def determine_trip_type(distance):
    if distance > 500:
        return 'Дальний рейс'
    return 'Обычный рейс'

name = input('Имя водителя: ')
distance = float(input("Расстояние: "))
fuel_consumption = float(input("Расход на 100 км: "))
price = float(input("Цена топлива: "))

fuel_needed = calculate_fuel(distance, fuel_consumption)
fuel_cost = calculate_cost(fuel_needed, price)
trip_type = determine_trip_type(distance)

print(f"Водитель: {name}")
print(f"Расстояние: {distance:.2f} км")
print(f"Тип рейса: {trip_type}")
print(f"Потребуется топлива: {fuel_needed:.2f} л")
print(f"Стоимость топлива: {fuel_cost:.2f} руб.")