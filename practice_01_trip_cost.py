name = input('Имя водителя: ')
distance = float(input("Расстояние: "))
fuel_consumption = float(input("Расход на 100 км: "))
price = float(input("Цена топлива: "))
fuel_needed = distance * fuel_consumption / 100
fuel_cost = fuel_needed * price

print(f"Водитель: {name}")
if distance > 500:
    trip_type = "Дальний рейс"
else:
    trip_type = "Обычный рейс"

print(f"Тип рейса: {trip_type}")
print(f"Потребуется топлива: {fuel_needed:.2f} л")
print(f"Стоимость топлива: {fuel_cost:.2f} руб.")