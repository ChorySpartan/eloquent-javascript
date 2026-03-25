#TUPLAS

dimensiones = (200, 50)
#dimensiones[0] = 45 // Acá intentamos modificar la tupla, pero esta es inmutable, es decir, que una vez
#creada no puede ser modificada

print(dimensiones[0])
print(dimensiones[1])

print('------------------------------------')
#RECORRIENDO LA TUPLA CON FOR

dimensiones2 = 200, 300, 100
for dimension in dimensiones2:
    print(dimension)

print('------------------------------------ \n')

#Si bien no pueden cambiarse los valores de una tupla, si los podemos reasignar

dimensiones3 = 1, 2, 3, 4, 5
print('Dimensiones originales: \n')
for dimension2 in dimensiones3:
    print(dimension2)

    dimensiones3 = 6, 7, 8, 9, 10
print('\n Dimensiones modificadas: \n')
for dimension2 in dimensiones3:
    print(dimension2)