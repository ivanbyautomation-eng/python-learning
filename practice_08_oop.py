class Driver:
    pass

ivan = Driver()
sacha = Driver()

class Truck:
    def __init__(self, brand, number, mileage):
        self.brand = brand
        self.number = number
        self.mileage = mileage


    def drive(self, distance):
        if distance > 0:
            self.mileage += distance
        else:
            print('Расстояние должно быть больше нуля!')

shacman =Truck('Shacman', "a111aa", 20000)
kamaz = Truck('Kamaz', 'a222aa', 10000)
man =Truck('Man', 'a333aa', 30000)

shacman.drive(1500)
kamaz.drive(300)
man.drive(2000)

print(shacman.mileage)
print(kamaz.mileage)
print(man.mileage)