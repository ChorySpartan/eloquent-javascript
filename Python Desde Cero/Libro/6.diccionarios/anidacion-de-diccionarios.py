#ANIDACIÓN

#Podemos anidar diccionarios dentro de una lista, una lista dentro de un diccionario o
#un diccionario dentro de otro diccionario

#UNA LISTA DE DICCIONARIOS

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'verde', 'puntos': '5', 'velocidad' : 'lento'}
    aliens.append(new_alien)

#Mostrando los primeros 5 aliens

for alien in aliens[:5]:
    print(alien)
print('...')

#Mostrando cuantos aliens fueron creados
print(f'El número total de aliens es: {len(aliens)}')

print('...')

#Para cambiar el color, la velocidad y los puntos de los tres primeros podemos usar un FOR y un IF

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'verde', 'puntos': '5', 'velocidad' : 'lento'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'verde':
        alien['color'] = 'pink'
        alien['velocidad'] = 'media'
        alien['puntos'] = '15'
        #Usando un ELIF para convertir los aliens amarillos a rojos
    elif alien['color'] == 'pink':
          alien['color'] = 'red'
          alien['velocidad'] = 'max'
          alien['puntos'] = '45'


#Mostrando los primeros 5 aliens

for alien in aliens[:5]:
    print(alien)
print('...')

#UNA LISTA EN UN DICCIONARIO

pizza = {
    'corteza': 'delgada',
    'ingredientes': ['jamón', 'queso extra', 'cebolla']
}

#Resumen del pedido

print(f'Ordenó una pizza {pizza["corteza"]} con los siguientes :')

for ingrediente in pizza["ingredientes"]:
    print('\t' + ingrediente)

print('----------------------')

favorite_languages5 = {
    'Jen' : ['Python', 'Ruby'],
    'Sarah' : ['C'],
    'Edward' : ['R', 'GO'],
    'Phil': ['Python', 'C++'],
}

for name, languages in favorite_languages5.items():
    #verificamos la cantidad de lenguajes con len()
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

print('----------------------')

#UN DICCIONARIO EN UN DICCIONARIO

users = {
    'AE': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'MC': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")






















