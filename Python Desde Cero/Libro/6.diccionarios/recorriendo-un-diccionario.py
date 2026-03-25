#RECORRIENDO TODOS LOS PARES CLAVE-VALOR

usuario = {
    'Nombre de Usuario' : 'Rodolfo',
    'Apellido' : 'Laynez',
    'Edad' : 32,
}

for k, v in usuario.items():
    print(f'\nClave: {k}')
    print(f'Valor: {v}')


lenguajes = {
    'Jen' : 'Python',
    'Sara' : 'C',
    'Edward' : 'R',
    'Phil': 'Python',
}

for nombre, lenguajes in lenguajes.items():
    print(f'El idioma favorito de {nombre.title()} es {lenguajes.title()}\n')


#RECORRIENDO TODAS LAS CLAVES DE UN DICCIONARIO

lenguajes2 = {
    'Jen' : 'Python',
    'Sara' : 'C',
    'Edward' : 'R',
    'Phil': 'Python',
}

for nombre2 in lenguajes2.keys():
    print(f'{nombre2.title()}\n')


favorite_languages = {
    'Jen' : 'Python',
    'Sarah' : 'C',
    'Edward' : 'R',
    'Phil': 'Python',
}

friends = ['Phil', 'Sarah']
for name in favorite_languages.keys():
    print(f'Hi {name.title()}')

    if name in friends:
        language = favorite_languages[name].title()
        print(f'\tHi {name.title()}, I see you love {language}!')


#Con esto podemos ver si algún parámetro no existe en el diccionario usando NOT IN

favorite_languages2 = {
    'Jen' : 'Python',
    'Sarah' : 'C',
    'Edward' : 'R',
    'Phil': 'Python',
}

if 'Erin' not in favorite_languages2.keys():
    print('Erin, please take our poll!\n')

print('__________________________________________\n')

#RECORRIENDO LAS CLAVES DE UN DICCIONARIO EN UN ORDEN PARTICULAR


favorite_languages3 = {
    'Jen' : 'Python',
    'Sarah' : 'C',
    'Edward' : 'R',
    'Phil': 'Python',
}
#Usando sorted() podemos ordenar en orden alfabético las claves del diccionario
for name in  sorted(favorite_languages3.keys()):
    print(f'{name.title()}, gracias por realizar la encuesta \n')



#RECORRIENDO TODOS LOS VALORES DE UN DICCIONARIO

favorite_languages4 = {
    'Jen' : 'Python',
    'Sarah' : 'C',
    'Edward' : 'R',
    'Phil': 'Python',
}

print('__________________________________________\n')

print('Se han mencionado los siguientes lenguajes:\n')
for favorite in favorite_languages4.values():
    print(favorite.title())

print('__________________________________________\n')

#Para evitar que se REPITA un valor debemos de usar


favorite_languages5 = {
    'Jen' : 'Python',
    'Sarah' : 'C',
    'Edward' : 'R',
    'Phil': 'Python',
}

print('Se han mencionado los siguientes lenguajes:\n')
for favorito in set(favorite_languages5.values()):
    print(favorito.title())

print('__________________________________________\n')

#PARA AGREGAR NUEVOS CLAVES VALOR USAMOS

favorite_languages5['Ciudad'] = 'Madrid'
print(favorite_languages5)

print('__________________________________________\n')

#Para agregar varios valores la mejor opción es hacerlo con update()

nuevos_datos = {
    'Pais' : 'Guatemala',
    'email' : 'rodolfo@gmail.com'
}

favorite_languages5.update(nuevos_datos)   # Acá le pasamos los valores de otro diccionario

print(favorite_languages5)











