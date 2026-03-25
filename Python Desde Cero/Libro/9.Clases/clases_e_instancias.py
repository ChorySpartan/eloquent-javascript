#TRABAJAR CON CLASES E INSTANCIAS


class Carro:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 50

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles > 0:  # La cantidad a añadir debe ser positiva
            self.odometer_reading += miles
        else:
            print("You can only add positive miles to the odometer!")

my_new_car = Carro('Audi', 'a4', 2025)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(50)
my_new_car.read_odometer()

print('----------------------------------------------')


#ESTABLECER UN VALOR PREDETERMINADO PARA UN ATRIBUTO

'''
    Cuando una instancia es creada, los atributos pueden ser definidos sin pasarlos como parámetros.
    Es decir que no van obligatoriamente dentro del __init__(parámetros)
    
    self.odometer_reading = 0  -- Este es un ejemplo, ya que no es un parámetro dentro de init
'''


#MODIFICAR VALORES DE LOS ATRIBUTOS

'''
    Se pueden cambiar los valores de un atributo de tres maneras:
        - Se puede cambiar el valor directamente a través de una instancia.
        - Se puede establecer el valor a través de un método.
        - Se puede incrementar el valor (agregarle una cierta cantidad) a través de un método. 
'''

#Modificando el valor de un atributo directamente

my_new_car2 = Carro('Toyota', 'Corolla', 2025)
my_new_car2.odometer_reading = 23  # <---- Se usa la notación de puntos para acceder al atributo
print(my_new_car2.get_descriptive_name())   # Y se establece el valor de este directamente.
my_new_car2.read_odometer()


print('----------------------------------------------')



#Modificando el valor de un atributo mediante un metodo

    #def update_odometer(self, mileage):
        #self.odometer_reading = mileage

#my_new_car.update_odometer(500)
#my_new_car.read_odometer()

'''
    Este es un método mediante el cual, el primer modelo pasa de tener 0 millas, como originalmente
    mostraba la función, a tener 500 millas, ya que se realizó una actualización por medio de un método.
    
    Esto sirve para evitar cambiar o actualizar determinados atributos, y en lugar de acceder al atributo
    directamente, se pasa el nuevo valor a un método que maneja la actualización internamente. 
'''


#Incrementar el valor de un atributo mediante un metodo


my_used_car = Carro('Honda', 'Civic', 2025)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

'''
    El método que se utilizó para actualizar el millaje del auto fue:
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
'''


#Ejercicio 9.4
























































































