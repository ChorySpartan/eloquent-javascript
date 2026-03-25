#DECLARACIÓN if SIMPLE

edad = 19
if edad >= 18:
    print('Tienes suficiente edad para votar')


#DECLARACIÓN if-else

edad2 = 17
if edad2 >= 18:
    print('\nTienes suficiente edad para votar')
else:
    print('\nLo siento, no tienes la edad legal para votar')

#DECLARACIÓN elif

edad3 = 122
if edad3 < 4:
    print('\nEl costo de entrada es gratuito')
elif edad3 < 18:        # elif se ejecutará solo si el if anterior falló, acá sí podemos agregar otra condición
    print('\nEl costo de entrada es de $25')
else:           # else no necesita que se agregue una condición
    print('\nEl costo de entrada es de $50')

#Esta es una mejor manera de hacer lo mismo que arriba

edad4 = 11

if edad4 < 4:
    precio = 0
elif edad4 < 18:
    precio = 25
else:
    precio = 50

print(f'El costo de la entrada es de ${precio}')


#USANDO MÚLTIPLES BLOQUES elif

edad5 = 66

if edad5 < 4:
    precio2 = 0
elif edad5 < 18:
    precio2 = 25
elif edad5 < 65:
    precio2 = 40
else:
    precio2 = 20

print(f'El costo de la entrada es de ${precio2}')

#Esta es una mejor forma de hacer lo de arriba sin usar el ELSE ya que no es necesario
#Se debe de analizar siempre si es o no necesario usarlo

edad5 = 66

if edad5 < 4:
    precio3 = 0
elif edad5 < 18:
    precio3 = 25
elif edad5 < 65:
    precio3 = 40
elif edad5 >= 65:
    precio3 = 10

print(f'El costo de la entrada es de ${precio3}')


#Si se quieren comprobar más de un bloque de código es necesario usar varios IF ya que si se usa ELIF
#solo se ejecutará hasta donde se pase la primer prueba en el código y los demás no se ejecutarán

requerir = ['Tortilla', 'Pan', 'Hojas', 'Pasta']
if 'Tortilla' in requerir:
    print('\nAgregando tortillas')
if 'Pan' in requerir:
    print('\nAgregando pan')
if 'Hojas' in requerir:
    print('\nAgregando hojas')

print('\nTerminaste de agregar los productos')



#  EJERCICIO

#5-3

alien_colors = 'Azul'

if alien_colors == 'Verde':
    print('\nEl jugador acaba de ganar 5 puntos')
elif alien_colors == 'Azul':
    print('\nEl jugador acaba de ganar 15 puntos')
else:
    print('\nEl jugador se murió')





















