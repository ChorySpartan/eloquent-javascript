#Creando clases

"""
    Crear un objeto a partir de una clase se llama creación de instancias y se trabaja con
    instancias de una clase.
"""


class Dog:

    def __init__(self, name, age,):
        #Esto inicializa los atributos de nombre y edad
        self.name = name
        self.age = age

    def sit(self):
        #Esto simula a un perro sentándose en respuesta a un comando
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        #Simular rodar en respuesta a un comando.
        print(f'{self.name} rolled over!.')



#CREANDO UNA INSTANCIA A PARTIR DE UNA CLASE

my_dog = Dog('Bob', 36)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age} years old.")



#Accediendo a los Atributos

'''
    my_dog.name   Podemos acceder a los atributos por medio de la notación de puntos
                  Esto es la instancia + un punto + el nombre del atributo asociado 
'''

#Métodos de Llamada

'''
    Después de crear una instancia en una clase, se puede usar la notación de puntos para llamar
    a cualquier método definido en ella.
'''

my_dog.sit()
my_dog.roll_over()


#CREANDO MÚLTIPLES INSTANCIAS

your_dog = Dog('Blacky', 5)

print(f'El nombre de mi perro es {my_dog.name}')
print(f'Mi perro tiene {my_dog.age} years old.')
my_dog.sit()

print(f'\nEl nombre de tu perro es {your_dog.name}')
print(f'Tu perro tiene {your_dog.age} years old.')
your_dog.sit()

print('-------------------------------------------')

#Ejercicio 9.1

class Restaurante:

    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.number_served = 0     # <--- ¡Agregado para el Ejercicio 9-4!
        self.set_number_served = 0

    def describe_restaurant(self):
        print(f'El nombre del restaurante es: {self.nombre_restaurante}.')
        print(f'El tipo de cocina es: {self.tipo_cocina}.')

    def open_restaurant(self):
        print(f'EL restaurante {self.nombre_restaurante} está abierto.')

restaurante = Restaurante('Pollo Campero', 'Cocina Chapina')

print(f'\nNombre del restaurante: {restaurante.nombre_restaurante}')
print(f'Tipo de cocina: {restaurante.tipo_cocina}')

print(f'\nLlamando a los métodos\n')
restaurante.describe_restaurant()
restaurante.open_restaurant()

print('-------------------------------------------')



#Parte del ejercicio 9.4

print(f'Clientes atendidos (inicial): {restaurante.number_served}')
restaurante.number_served = 500_000
print(f'Clientes atendidos (después del cambio): {restaurante.number_served}')

print('-------------------------------------------')

restaurante.set_number_served = 100
print(f'Clientes atendidos: {restaurante.set_number_served}')

print('-------------------------------------------')

#Ejercicio 9.2

restaurante2 = Restaurante('Pollo Brujo', 'Cocina al Carbón')
restaurante3 = Restaurante('La Trama', 'Cocina de Hamburguesas')
restaurante4 = Restaurante('Bonanza', 'Cocina Gourmet')

restaurante2.describe_restaurant()
restaurante3.describe_restaurant()
restaurante4.describe_restaurant()

print('-------------------------------------------\n')

class Usuario:

    def __init__(self, nombre, apellido, edad, correo, usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.usuario = usuario

    def describe_users(self):
        print(f'El nombre es: {self.nombre}, el apellido es: {self.apellido}, ' 
              f'la edad del usuario es: {self.edad}, el correo es: {self.correo} '
              f'y el usuario es: {self.usuario}')

    def greet_user(self):
        print(f'Bienvenido {self.usuario}, por favor presione "enter" para continuar.')

usuario1 = Usuario('Rodolfo', 'Laynez', 32, 'rodolfolaynez@hotmail.com',
                                            'ChorySpartan')
usuario2 = Usuario('Maythe', 'Jiménez', 18, 'maygatopate@gmail.com',
                   'Gatito')


usuario1.describe_users()
usuario1.greet_user()
usuario2.describe_users()
usuario2.greet_user()

print('-------------------------------------------\n')


class IceCreamStand(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina,):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = ['Vainilla', 'Crema', 'Fresa', 'Limón']


    def describe_sabores(self):
        print(f'Los sabores disponibles actualmente son: {self.sabores}')

tipos = IceCreamStand("Sarita", "Heladería")
tipos.describe_sabores()
tipos.open_restaurant()


















































