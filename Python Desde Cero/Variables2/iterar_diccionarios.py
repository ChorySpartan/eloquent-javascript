diccionario = {
    'nombre': 'Rodolfo',
    'apellido': 'Laynez',
    'subs': 1000,
}

for key in diccionario.items():
    print(key)

diccionario2 = {
    'nombre': 'Alejandro',
    'apellido': 'Laynez',
    'edad': 1
}

for datos in diccionario2.items():
    key2 = datos[0]
    value = datos[1]
    print(f'La clave es: {key2} y el valor es: {value}')

#Esto me muestra solo las llaves
for keys in diccionario2.keys():
    print(keys)