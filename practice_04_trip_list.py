

def calculate_fuel(distance, fuel_consumption):
    return distance * fuel_consumption / 100


def calculate_cost(fuel_needed, price):
    return fuel_needed * price


def determine_trip_type(distance):
    if distance > 500:
        return 'Дальний рейс'
    return 'Обычный рейс'

def read_positive_number(prompt):
    while True:
        try:
            number = float(input(prompt))

            if number <= 0:
                print('Ошибка: число должно быть больше нуля.')
                continue
            return number

        except ValueError:
            print("Ошибка: введите число.")


trips = []

while True:

    driver_name = input('Имя водителя: ')
    distance_km = read_positive_number("Расстояние: ")
    fuel_consumption = read_positive_number("Расход на 100 км: ")
    fuel_price = read_positive_number("Цена топлива: ")

    fuel_needed = calculate_fuel(distance_km, fuel_consumption)
    fuel_cost = calculate_cost(fuel_needed, fuel_price)
    trip_type = determine_trip_type(distance_km)

    trip = {
        "driver_name": driver_name,
        "distance_km": distance_km,
        "fuel_consumption": fuel_consumption,
        "fuel_price": fuel_price,
        "fuel_needed": fuel_needed,
        "fuel_cost": fuel_cost,
        "trip_type": trip_type,
    }

    trips.append(trip)

    answer = input("Добавить ещё один рейс? (да/нет): ")

    if answer.lower() != "да":
        break


print("\nСписок рейсов:")

for trip_number, trip in enumerate(trips, start=1):
    print(f"\nРейс №{trip_number}")
    print(f"Водитель: {trip['driver_name']}")
    print(f"Расстояние: {trip['distance_km']:.2f} км")
    print(f"Тип рейса: {trip['trip_type']}")
    print(f"Потребуется топлива: {trip['fuel_needed']:.2f} л")
    print(f"Стоимость топлива: {trip['fuel_cost']:.2f} руб.")


total_distance = sum(trip["distance_km"] for trip in trips)
total_fuel_needed = sum(trip["fuel_needed"] for trip in trips)
total_fuel_cost = sum(trip["fuel_cost"] for trip in trips)

print("\nОбщая статистика:")
print(f"Количество рейсов: {len(trips)}")
print(f"Общее расстояние: {total_distance:.2f} км")
print(f"Всего потребуется топлива: {total_fuel_needed:.2f} л")
print(f"Общая стоимость топлива: {total_fuel_cost:.2f} руб.")