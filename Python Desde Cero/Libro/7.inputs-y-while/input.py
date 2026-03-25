#INPUT

mensaje = input('Dime algo y lo repetiré')
print(mensaje)

#ESCRIBIR INDICACIONES CLARAS

nombre2 = input('Ingrese su nombre: ')
print(f'\nHola, {nombre2}!')

#PODEMOS ASIGNAR UN MENSAJE A UNA VARIABLE, Y LA VARIABLE PASARLA AL INPUT

nombre3 = 'Si comparte su nombre, podemos personalizar los mensajes que ve.'
nombre3 += '\n¿Cuál es tu primer nombre? '

name = input(nombre3)
print(f'\nHola, {name}')

age = input('Ingrese su edad: ')
age = int(age)
print(age >= 18)

#EL OPERADOR DE MÓDULO % % % % %

numero = input('Ingrese un numero y te diré si es par o impar: ')
numero = int(numero)
if numero % 2 == 0:
    print(f'\nEl número {numero} es par.')
else:
    print(f'\nEl numéro {numero} es impar.')













































