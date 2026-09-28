import json

try:
    with open('example.json', 'r', encoding='utf-8') as file:
        drivers = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
    drivers = []

while True:
    name = input('Введите имя: ').strip()
    if name:
        break
    print('Имя не может быть пустым!')

while True:
    try:

        distance = float(input('Введите расстояние: '))
        if distance <= 0:
            print('Расстояние должно быть больше нуля!')
            continue

        break

    except ValueError:
        print('Нужно ввести число!')

data = {'name': name,
        'distance': distance}

drivers.append(data)

with open('example.json', 'w', encoding='utf-8') as file:
    json.dump(drivers, file, ensure_ascii=False, indent=4)