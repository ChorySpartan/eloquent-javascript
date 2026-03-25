#CREANDO UNA FUNCIÓN QUE NOS DEVUELVA LOS NÚMEROS PRIMOS ENTRE 0 Y EL ARGUMENTO QUE PASAMOS

#Esto es una función que verifica si un número es primo
def es_primo(num):
    #Verificamos que el número pasado no pueda dividirse por ningún número entre 2 y ese mismo número -1
    for i in range(2, num - 1):
        #Si es divisible por alguno retorna False y se termina el bucle
        if num % i == 0: return False
    #Si termina el bucle, significa que no fue divisible, entonces es primo
    return True

#Creando una función que retorne una lista con todos los números primos
def primos_hasta(num):
    #Creación de la lista
    primos = []
    for i in range(3, num + 1):
        #Verificamos si el valor es un número primo
        resultado = es_primo(i)
        #En caso de que sea un número primo se agrega a la lista
        if resultado == True: primos.append(i)
    #Esto devuelve la lista
    return primos

#Creamos el resultado llamando a la función y lo mostramos
resultado = primos_hasta(13)
print(resultado)



#Esta es una FUNCIÓN ANIDADA, hace lo mismo que arriba pero con menos código
primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))
print(primos_hasta(15))
















































































