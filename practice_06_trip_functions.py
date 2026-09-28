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


def read_driver_name():
    while True:
        name = input("Имя водителя: ").strip()

        if name:
            return name

        print("Ошибка: имя не может быть пустым.")


def create_trip():
    driver_name = read_driver_name()
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

    return trip


def print_trip(trip_number, trip):
    print(f"\nРейс №{trip_number}")
    print(f"Водитель: {trip['driver_name']}")
    print(f"Расстояние: {trip['distance_km']:.2f} км")
    print(f"Тип рейса: {trip['trip_type']}")
    print(f"Потребуется топлива: {trip['fuel_needed']:.2f} л")
    print(f"Стоимость топлива: {trip['fuel_cost']:.2f} руб.")



def print_all_trips(trips):
    print("\nСписок рейсов:")
    for trip_number, trip in enumerate(trips, start=1):
        print_trip(trip_number, trip)


def calculate_statistics(trips):
    total_distance = sum(trip["distance_km"] for trip in trips)
    total_fuel_needed = sum(trip["fuel_needed"] for trip in trips)
    total_fuel_cost = sum(trip["fuel_cost"] for trip in trips)

    statistics = {
        "trip_count": len(trips),
        "total_distance": total_distance,
        "total_fuel_needed": total_fuel_needed,
        "total_fuel_cost": total_fuel_cost,
    }
    average_distance = (
            statistics["total_distance"] / statistics["trip_count"]
    )

    return statistics, average_distance


def analyze_trips(trips):
    long_trip_count = 0
    regular_trip_count = 0
    most_expensive_trip = trips[0]
    most_expensive_trip_number = 1

    for trip_number, trip in enumerate(trips, start=1):
        if trip['distance_km'] > 500:
            long_trip_count += 1
        else:
            regular_trip_count += 1

        if trip['fuel_cost'] > most_expensive_trip['fuel_cost']:
            most_expensive_trip = trip
            most_expensive_trip_number = trip_number


    analysis = {
            "long_trip_count": long_trip_count,
            "regular_trip_count": regular_trip_count,
            "most_expensive_trip": most_expensive_trip,
            "most_expensive_trip_number": most_expensive_trip_number
    }

    return analysis

def main():
    trips = []

    while True:

        trip = create_trip()
        trips.append(trip)

        answer = input("Добавить ещё один рейс? (да/нет): ")

        if answer.strip().lower() != "да":
            break

    statistics, average_distance = calculate_statistics(trips)

    print_all_trips(trips)
    analysis = analyze_trips(trips)

    print("\nОбщая статистика:")
    print(f"Количество рейсов: {statistics['trip_count']}")
    print(f"Общее расстояние: {statistics['total_distance']:.2f} км")
    print(f"Всего потребуется топлива: {statistics['total_fuel_needed']:.2f} л")
    print(f"Общая стоимость топлива: {statistics['total_fuel_cost']:.2f} руб.")


    print('\nАнализ рейсов: ')
    print(f"Дальних рейсов: {analysis['long_trip_count']}")
    print(f"Обычных рейсов: {analysis['regular_trip_count']}")
    print(f"Среднее расстояние: {average_distance:.2f} км")

    print('\nСамый дорогой рейс: ')
    print(f"Номер рейса: {analysis['most_expensive_trip_number']}")
    print(f"Водитель: {analysis['most_expensive_trip']['driver_name']}")
    print(f"Стоимость: {analysis['most_expensive_trip']['fuel_cost']:.2f} руб")


main()