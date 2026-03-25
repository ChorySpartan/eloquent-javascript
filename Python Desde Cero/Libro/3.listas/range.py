#RANGE

#En este caso solo devolverá los números del 1 al 4
#El primer valor es el número en donde empezará, en este caso es el número 1
#El segundo argúmento es en donde debe de terminar

for value in range(1, 5):
    print(value)

#Esto nos devuelve una lista con los números en range
numeros = list(range(1, 5))
print(numeros)

#Si se le pasa un tercer argumento, este se sumará hasta llegar al resultado final
numeros_pares = list(range(5, 17, 1))
print(numeros_pares)

#Si  le pasamos un solo argumento a range, este empezará a contar desde cero
numeros_desde_cero = range(6)
print(numeros_desde_cero)

#Con range podríamos mostrar la potencia en los primeros 10 números con este ejemplo
cuadrados = []
for value in range(1, 11):
    cuadrado = value **2
    cuadrados.append(cuadrado)
    print(cuadrado)

print('___________________')

#ESTA ES UNA MEJOR FORMA DE HACER LO MISMO

cuadrados2 = []
for value in range(1, 11):
    cuadrados2.append(value**2)
    print(cuadrados2)