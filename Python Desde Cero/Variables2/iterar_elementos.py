animales = ['gato', 'perro', 'loro', 'cocodrilo']
numeros = [1, 2, 3, 4, 5]

#Reccorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')


#Recorriendo la lista números y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)


#Para iterar ambas listas o más de una lista al mismo tiempo

#Esto se va a iterar al mismo tiempo siempre
#for numero, animal in zip(numeros, animales):
    # print(f'recorriendo lista 1: {numero}')
    # print(f'recorriendo lista 2: {animal}')



#Esto permite usar RANGE para recorrer cierto listado de números
for num in range(1, 11):
    print(num)


#FORMA CORRECTA de recorrer una lista con su índice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El índice es: {indice} y el valor es: {valor}')

#Ejemplo desafío

animales2 = ['gato', 'perro', 'loro', 'cocodrilo']
for numeracion, nombre in enumerate(animales2):
    print(f'El nombre es: {nombre} y su índice es {numeracion}')

#USANDO for Y else

for numero in numeros:
    print(f'Ejecutando el último bucle, valor actual: {numero}')
else:
    print('El bucle terminó')

#NO PODEMOS RECORRER CONJUNTOS {}












































