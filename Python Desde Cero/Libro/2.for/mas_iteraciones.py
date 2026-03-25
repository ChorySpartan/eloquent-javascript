#Creando las listas

frutas = ['banana', 'manzana', 'pera', 'ciruela', 'naranja', 'granada', 'durazno']
cadena = 'Hola Rodolfo'
numeros = [1, 2, 3, 4, 5]


#continue sirve para que se salte algo en específico que nosotros asignamos

for fruta in frutas:
    if fruta == 'manzana':
        continue                #Esto evita que se itere 'manzana' en el código
    print(f'Me voy a comer una {fruta}')

print('---------------------------------')


#break sirve para que el bucle se siga ejecutando, si se cumple la condición se detendrá
#Si después del break hay algún else no se va a ejecutar si se cumple la condición
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voy a comer una {fruta}')

print('Bucle terminado')

print('---------------------------------')


#Recorriendo un STRING

for letra in cadena:
    print(letra)

print('---------------------------------')


#FOR en una sola línea de código

#Con esto podríamos duplicar valores en una lista de números

numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)

print(numeros_duplicados)

print('---------------------------------')

#Pero para hacerlo con una línea se hace con

numeros_duplicados2 = [x*2 for x in numeros]
print(numeros_duplicados2)

print('---------------------------------')


#FOR en una línea para strings

nombres = ['Ana', 'Luis', 'Carlos',]

nombres_mayus = [nombre.upper() for nombre in nombres]
print(nombres_mayus) # ['ANA', 'LUIS', 'CARLOS']

print('---------------------------------')


#FOR en una línea para tuplas

coordenadas = [(1, 2), (3, 4), (5, 6)]

x_dobles = [x*2 for (x, y) in coordenadas]
print(x_dobles) # [2, 6, 10]

print('---------------------------------')


#FOR en una líena con condicionales

edades = [12, 17, 18, 21,]

mayores = [edad for edad in edades if edad >= 18]

print(mayores) # [18, 21]

print('---------------------------------')


#FOR en una línea con diccionarios

precios = {
    'manzana': 1.0,
    'pera': 2.0,
    'ciruela': 3.0,
}

con_iva = {
    producto: round(precio * 1.12, 2) for producto, precio in precios.items()
}

print(con_iva)








