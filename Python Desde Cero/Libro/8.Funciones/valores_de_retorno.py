#VALORES DE RETORNO


#Devolver un Valor Simple

def nombre_ordenado(primer_nombre, apellido):
    #Esto devuelve el nombre formateado
    nombre = f'{primer_nombre} {apellido}'
    return nombre.title()

musico = nombre_ordenado('Rodolfo', 'Laynez')
print(musico)

print('________________________________________')


#Hacer que un argumento sea opcional

def nombre_ordenado2(primer_nombre, apellido, segundo_nombre = ''):
    #Esto retorna el nombre completo y formateado
    if segundo_nombre:
        nombre_completo = f'{primer_nombre} {segundo_nombre} {apellido}'
    else:
        nombre_completo = f'{primer_nombre} {apellido}'
    return nombre_completo.title()

musico2 = nombre_ordenado2('Rodolfo', 'Laynez')
print(musico2)

musico2 = nombre_ordenado2('Rodolfo', 'Laynez', 'S')
print(musico2)

print('________________________________________')


#Devolviendo un Diccionario

def persona(primer_nombre, apellido, edad = None):
    #Esto retorna los valores como un diccionario
    persona = {'Primero': primer_nombre, 'Segundo': apellido}
    if edad:
        persona['edad'] = edad
    return persona

musico4 = persona('Rodolfo', 'Laynez', edad = 32)
print(musico4)

print('________________________________________')



#Usando una función con un bucle WHILE


def get(first_name, last_name):
    full = f'{first_name} {last_name}'
    return full.title()

while True:
    print('\nPlease tell me your name: ')
    print('Si quiere salir del programa, por favor escriba "esc" ')
    f_name = input('First name: ')
    if f_name == 'esc':
        break
    l_name = input('Last name: ')
    if l_name == 'esc':
        break


    formatted_name = get(f_name, l_name)
    print(f'\nHello {formatted_name}')


#Ejercicio 8.6

def city_country(ciudad, pais):
    nombre2 = f'{ciudad} {pais}'
    return nombre2.title()

nombre_ciudad = city_country('Quiché,', 'Guatemala')
nombre_ciudad2 = city_country('Guadalajara,', 'México')
nombre_ciudad3 = city_country('Toronto,', 'Cánada')


print(nombre_ciudad)
print(nombre_ciudad2)
print(nombre_ciudad3)


#Ejercicio 8.7

def make_album(artista, titulo, canciones = None):
    album = {'Artista': artista, 'Titulo': titulo}
    if canciones:
        album['Canciones'] = canciones
    return album

while True:
    print('\nPor favor, ingrese el artista y el título del albúm: ')
    print('Para salir escriba "salir"')

    artista1 = input('Artista: ')
    if artista1.lower() == 'salir':
        break

    titulo1 = input('Nombre del disco: ')
    if titulo1.lower() == 'salir':
        break

    disco = make_album(artista1, titulo1)
    print(f'El albúm creado es: {disco}')














































