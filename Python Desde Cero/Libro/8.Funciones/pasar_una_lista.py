#PASANDO UNA LISTA A UNA FUNCIÓN

def greet_user(names):
    for name in names:
        msg = f'Hello, {name.title()}'
        print(msg)

usernames = ['Rodolfo', 'Alejandro', 'Adriana']
greet_user(usernames)

print('-----------------------------------------------')



#MODIFICAR UNA LISTA EN UNA FUNCIÓN

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Printing model: {current_design}')
    completed_models.append(current_design)

print('\nThe following models have been printed:')
for completed_model in completed_models:
    print(completed_model)

print('-----------------------------------------------1')

#Estas dos funciones hacen lo mismo que arriba, si bien es más código es la mejor opción para
#obtener el resultado requerido, ya que podemos llamar a ambas funciones varias veces
def print_models(unprinted_designs2, completed_models2):
    while unprinted_designs2:
        current_design2 = unprinted_designs2.pop()
        print(f'Printing model: {current_design2}')
        completed_models2.append(current_design2)

def show_completed_models(completed_models2):
    print(f'\nThe following models have been printed:')
    for completed_model2 in completed_models2:
        print(completed_model2)

unprinted_designs2 = ['phone case', 'robot pendant', 'dodecahedron']
completed_models2 = []

print_models(unprinted_designs2, completed_models2)
show_completed_models(completed_models2)

print('-----------------------------------------------')

#Así se REUTILIZA una función, en este caso las funciones son 'print_models' y 'show_completed_models'
#creamos una nueva lista y una lista vacía y esas variables las pasamos como nuevos argumentos
lista = ['a', 'b', 'c']
completed_models3 = []

print_models(lista, completed_models3)
show_completed_models(completed_models3)

print('-----------------------------------------------')


#EVITAR QUE UNA FUNCIÓN MODIFIQUE UNA LISTA

#Para evitar que se vacíe una lista por completo podemos crear una copia
#Para esto utilizamos [:] después del argumento dentro del llamado de la función

lista2 = ['1', '2', '3']
completed_models4 = []

print_models(lista2[:], completed_models4)
show_completed_models(completed_models4)

print('-----------------------------------------------')

print(lista) #Como se utilizó normalmente la función, la lista se mostrará vacía []

print(lista2) #En este caso, la lista seguirá mostrando su contenido porque pasamos una copia

print('-----------------------------------------------')


#Ejercicio 8.9

def mensajes_cortos(mensajes):
    for mensaje in mensajes:
        msg1 = f'Hola, {mensaje}'
        print(msg1)

mensaje_de_usuarios = ['me llamo Rodolfo', 'me llamo Alejandro', 'me llamo Extraterrestre']
mensajes_cortos(mensaje_de_usuarios)

print('-----------------------------------------------')


#Ejercicio 8.10

mensajes_enviados = []

def send_messages(messages, enviados_a_la_nueva_lista):
    while messages:
        mensaje_actual = messages.pop(0)
        print(f'Enviando mensaje: {mensaje_actual}')
        enviados_a_la_nueva_lista.append(mensaje_actual)

send_messages(mensaje_de_usuarios[:], mensajes_enviados)

print('\nMensajes originales (debería estar vacía:) ')
print(mensaje_de_usuarios)

print('\nMensajes enviados: ')
print(mensajes_enviados)



































































