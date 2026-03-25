#DICCIONARIO SENCILLO

alien = {'color': 'green', 'points': 5}
# El primer dato es una clave y el que va después es el valor clave:valor

print(alien['color'])
print(alien['points'])

nuevos_puntos = alien['points']
print(f'Acabas de ganar {nuevos_puntos} puntos')


#AGREGANDO NUEVOS PARES clave:valor

alien2 = {'color': 'green', 'points': 5}
print(alien2)

alien2['x_position'] = 0
alien2['y_position'] = 25
print(alien2)


#DICCIONARIOS VACÍOS

alien3 = {}

alien3['color'] = 'green'
alien3['points'] = 5
print(alien3)


#MODIFICAR LOS VALORES EN UN DICCIONARIO

alien4 = {'color': 'green'}
print(f'El extraterrestre es {alien4["color"]}')

alien4['color'] = 'yellow'
print(f'El extraterrestre ahora es {alien4["color"]}')


alien4 = {'x_position': 0, 'y_position': 25, 'velocidad': ''}
print(f'Posición original: {alien4["x_position"]}')

#Mover el extraterrestre hacia la derecha
#Determinar qué tan lejos mover al extraterrestre en función de su velocidad actual

if alien4['velocidad'] == 'lento':
    incremento_x = 1
elif alien4['velocidad'] == 'media':
    incremento_x = 2
else:
    #Esto sería la velocidad rápida
    incremento_x = 3

#Nueva posición más el incremento
alien4['x_position'] = alien4['x_position'] + incremento_x
print(f'La nueva posición es: {alien4["x_position"]}')



#UN DICCIONARIO DE OBJETOS SIMILARES

lenguajes = {
    'Jen' : 'Python',
    'Sara' : 'C',
    'Edward' : 'R',
    'Phil': 'Python',
}

lenguaje = lenguajes['Sara'].title()
print(f'El lenguaje favorito de Sara es {lenguaje}')


#USANDO get() PARA ACCEDER A VALORES EN EL DICCIONARIO

metodo_get = {
    'Color' : 'Green',
    'Velocidad' : 'Lento'
}

#Debemos de usar get si no estamos seguros de que exista la clave que queremos llamar en el diccionario
puntos = metodo_get.get('Puntos', 'No se ha asignado ningún valor de puntos')
print(puntos)


diccionario5 = {
    'Nombre' : 'Rebeca',
    'Apellido' : 'Rámirez',
    'Edad' : 29,
    'Ciudad' : 'Jalisco',
}

print(diccionario5)

diccionario6 = {
    'Magdalena' : 14,
    'Javi' : 213,
    'Richard' : 32,
    'Teresa' : 23,
}

clave_diccionario6 = diccionario6['Magdalena']
print(f'El lenguaje favorito de Magdalena es {clave_diccionario6}')
































