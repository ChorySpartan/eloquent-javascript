#USANDO UN BUCLE while CON LISTAS Y DICCIONARIOS

#MOVIENDO ELEMENTOS DE UNA LISTA A OTRA

unconfirmed_users = ['alice', 'brian', 'candy']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

print(f'\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#ELIMINAR TODAS LAS INSTANCIAS DE VALORES ESPECÍFICOS DE UNA LISTA

mascotas = ['perro', 'gato', 'pez', 'gato', 'caballo', 'gato', 'conejo', 'gato',]
print(mascotas)

while 'gato' in mascotas:
    mascotas.remove('gato')

print(mascotas)

#LLENAR UN DICCIONARIO CON ENTRADAS DEL USUARIO

respuestas  = {}

polling_active = True

while polling_active:
    name = input('\n¿Cuál es tu nombre?')
    respuesta = input('¿Qué montaña te gustaría escalar algún día?')

# En esta línea (40) se guardan los clave-valor del diccionario que son los dos inputs de arriba
    respuestas[name] = respuesta

    repeat = input('¿Te gustaría dejar que otra persona responda? (sí / no) ')
    if repeat.lower().strip() == 'no':
        polling_active = False

print('\n--- Resultados ---')
for name, response in respuestas.items():
    print(f'{name}: le gustaría escalar {response}.')

print(respuestas)















































