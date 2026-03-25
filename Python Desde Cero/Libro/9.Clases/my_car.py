from car import Car3, ElectricCar2

my_new_car = Car3('Mitsubishi', 'Lancer', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=230
my_new_car.read_odometer()

carro_electrico = ElectricCar2('Toyota', 'Eléctrico', 2025)
print(carro_electrico.get_descriptive_name())