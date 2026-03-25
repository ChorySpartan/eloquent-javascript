#HERENCIA

print()

'''
    Si la clase que estás escribiendo es una versión especializada de otra clase que escribiste, 
    puedes usar la herencia. Cuando una clase hereda de otra, adopta los atributos y métodos de 
    la primera clase. La clase original se llama clase principal y la nueva clase es clase secundaria. 
    La clase hija puede heredar cualquiera o todos los atributos y métodos de su clase padre, pero 
    también es libre de definir nuevos atributos y métodos propios
'''


#EL METODO __init__() PARA UNA CLASE SECUNDARIA

class Car2:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading2 = 0

    def get_descriptive_name2(self):
        long_name2 = f'{self.year} {self.make} {self.model}'
        return long_name2

    def read_odometer2(self):
        print(f'This car has {self.odometer_reading2} miles on it.')

    def update_odometer2(self, mileage2):
        if mileage2 >= self.odometer_reading2:
            self.odometer_reading2 = mileage2
        else:
            print('You can´t roll back an odometer!')

    def increment_odometer2(self, miles):
        self.odometer_reading2 += miles

    def gas_tank(self):     #   <---------- Este es un metodo, no es únicamente la línea de self en sí
        print('This car has a 75-liter gas tank.')         #Sino que es una función en sí que se puede sobreescribir


class Battery:
    def __init__(self, battery_size=65):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        if self.battery_size <= 100:
            range = 260
        elif 100 < self.battery_size <= 200:
            range = 315
        print(f'This car can go about {range} miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size != 65:
            print(f'Actualizando la batería de {self.battery_size}-kWh a 65 kWh.')
            self.battery_size = 65
        else:
            print(f'La batería ya es de 65 kWh, no se necesita una actualización')

class ElectricCar(Car2):   # <------ Para la subclase debemos de agregar entre paréntesis el nombre
                           # de la superclase, en este caso Car2
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    #def describe_battery(self):
        #print(f'This car has a {self.battery_size}-kWh battery.')

    def gas_tank(self):         # Acá sobreescribimos el metodo de gas_tank, por lo que se ignora el primero
        print("This car doesn't need a gas tank!")      # y se ejecuta este.


my_tesla = ElectricCar('Tesla', 'Model S', 2025)
print(my_tesla.get_descriptive_name2())
#my_tesla.describe_battery()
my_tesla.gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#DEFINICIÓN DE ATRIBUTOS Y MÉTODOS PARA LA CLASE SECUNDARIA

'''
    Una vez que tenga una clase secundaria que herede de una clase principal, puede agregar
    todos los atributos y métodos nuevos necesarios para diferenciar la clase secundaria de la
    clase principal.
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75  <-------------Esto fue lo que se agregó en esta sección
'''


#ANULACIÓN DE MÉTODOS DE LA CLASE PRINCIPAL

'''
    Para sobrescribir (override) un método de la clase padre (superclase) en la clase hija (subclase), 
    debes escribir un método en la subclase con el mismo nombre que el método que deseas sobrescribir 
    en la clase padre.

    Python, al encontrar un método con el mismo nombre en la subclase, ignorará el método de la clase 
    padre y ejecutará el método definido en la subclase cuando lo llames desde una instancia de la subclase.
'''



#INSTANCIAS COMO ATRIBUTOS

'''
    Las instancias como atributos, también conocido como composición en la Programación Orientada a 
    Objetos (POO), es una forma poderosa de modelar relaciones donde un objeto "tiene un" (has-a) u 
    "está compuesto de" otro objeto. En lugar de heredar características de otra clase, una clase crea 
    y almacena una instancia de esa otra clase como uno de sus propios atributos.

    Imagina que estás construyendo un coche. Un coche puede tener muchas partes: un motor, un volante, 
    ruedas, una batería, etc. No dirías que un Coche es un Motor (eso sería herencia), sino que un 
    Coche tiene un Motor. En este caso, el Motor sería una instancia que es un atributo del Coche.
'''


#Ejercicio 9.6























































































