#Comprobar si un valor está en una lista

ingredientes = ['Queso', 'Cebollas', 'Tomate', 'Masa']
if 'queso' in [i.lower() for i in ingredientes]:
    print('Vamos a comer mucha pizza con mucho queso hoy')


#Esto también se puede hacer de otra manera con:

ingrediente_buscado = 'queso'

for item in ingredientes:
    if item.lower() == ingrediente_buscado.lower():
        print('\nSí hay queso, ¡y en cantidades industriales!')
    else:
        if item not in ingredientes:
            print('\nno se encuentra el ingrediente')


#COMPROBANDO LA DESIGUALDAD

request = 'salsa'
if request != 'parmesano':
    print('\nNo se seguirá con la orden')



#COMPARACIONES NUMÉRICAS

edad = 20
if edad != 42:
    print('\nEdad incorrecta')

#COMPARACIÓN DE MÚLTIPLES CONDICIONES CON and Y or

edad1 = 35
edad2 = 22

if edad1 >= 20 and edad2 >= 20:
    print('\nEdad correcta')

edad3 = 50
edad4 = 1
if edad3 >= 50 or edad4 >= 50:
    print('\nEdad incorrecta')

#COMPROBACIÓN CON in

ingredientes2 = ['frijol', 'maíz', 'arroz', 'trigo']
if 'frijol' in ingredientes2:
    print('\nCocoi, Cocoi')
if 'salsa' not in ingredientes2:
    print('\nNo se encuentra el ingrediente')



































