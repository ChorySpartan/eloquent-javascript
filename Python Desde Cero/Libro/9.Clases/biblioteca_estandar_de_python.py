#LA BIBLIOTECA ESTÁNDAR DE PYTHON

#randint()

'''
    Esta función nos sirve para generar un número entero aleatorio dentro de un rango específicado,
    incluyendo ambos extremos del rango.
'''

from random import randint, choice
import random

randint(1,6)
print(randint(1,6))

#choice()

'''
    Es una función que también forma parte del módulo "random" así como "randint()". Sirve para seleccionar
    un elemento aleatorio de una secuencia no vacía, como una lista, una tupla o una cadena.
'''
players = ['Carlos', 'Rodolfo', 'Alejandro', 'Michael', 'Eli']
first_up = choice(players)
print(first_up)


#Ejercicio 9.13

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

dice = Die()
print(dice.roll_die())

dice_10 = Die(sides=10)
print(dice_10.roll_die())

dice_20 = Die(sides=20)
print(dice_20.roll_die())



#Ejercicio 9.14

elementos_loteria = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# sample() evitará que se seleccione varias veces el mismo elemento de la lista.
# choice() elegirá un único valor de la secuencia, es decir de la lista, tupla, cadena, etc.
# choices() elegirá los valores que le asignemos, es decir si agregamos a = 4 nos mostrara cuatro elementos.
# y siempre debe de llevar k=número ya que no funciona con otra letra.
numeros_ganadores = random.choices(elementos_loteria, k=6)

print(f"Los números/letras ganadores son: {numeros_ganadores}")
print("¡Cualquier boleto que coincida con estos 4 números/letras gana un premio!")



#Ejercicio 9.15

my_ticket = random.sample(numeros_ganadores, k=6)
print(f'Mi boleto de lotería es: {my_ticket}')

winning_ticket = []
attempts = 0

while winning_ticket != my_ticket:
    winning_ticket = random.sample(numeros_ganadores, k=6)
    attempts += 1

print(f'\n¡Felicidades! Tu boleto {my_ticket} ha ganado la lotería.')
print(f'Se necesitaron {attempts} intentos para obtener un boleto ganador.')

























































