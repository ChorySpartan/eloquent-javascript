# Este se va a ejecutar mientras una determinada condición continue siendo verdadera

numero = 1
while numero <= 1000:
    print(numero)
    numero += 1

#PERMITIR QUE EL USUARIO ELIJA CUÁNDO SALIR

prompt = '\nDime algo y te lo repetiré: '
prompt += '\nEnter "quit" to end the program. '

message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)

print('-------------------------------')


prompt = '\nDime algo y te lo repetiré: '
prompt += '\nEnter "quit" to end the program. '

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)

print('-------------------------------')


# USO DE BREAK PARA SALIR DE UN BUCLE


prompt = '\nDime algo y yo lo diré de nuevo: '
prompt += '\nEnter "finish" to end the program. '

while True:
    city = input(prompt)
    if city == "finish":
        break
    else:
        print(f"Amo ir a la {city.title()}!")


#USO DE continue

numero = 0
while numero <= 100:
    numero += 1
    if numero % 2 == 0:
        continue

    print(numero)


#EVITAR BUCLES INFINITOS

mensaje = '\nPor favor, ingrese un ingrediente. '
mensaje += '\nPara salir, escriba "end". '

while True:
    mensaje_1 = input(mensaje)
    if mensaje_1 == 'end':
        break
    else:
        print(f"El ingrediente que seleccionó es {mensaje_1.title()}")


#7-5

prompt1 = '\nPor favor ingrese su edad: '
prompt1 += '\nPara salir, escriba "finalizar". '

while True:
    mensaje_2 = input(prompt1)
    if mensaje_2 == 'finalizar':
        print('Gracias por usar el sistema de precios de entradas.')
        break

    edad = int(mensaje_2)

    if edad < 3:
        precio = '$0'
    elif 3 <= edad <= 12:
        precio = '$10'
    elif edad > 12:
        precio = '$15'

    print(f'El costo de su entrada es de: {precio}')






























