#Creando funciones LAMBDA

multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5))


#Creando una función que muestre los pares o impares

numeros = [1,2,3,4,5]
def es_par(num):
    if num % 2 == 0:
        return True

numeros_pares = filter(es_par, numeros)

print(list(numeros_pares))

#Creando la misma función pero con LAMBDA pero con números impares

numeros2 = [1, 2, 3, 4, 5]

numeros_impares = filter(lambda numero : numero % 2 == 1, numeros2)
print(list(numeros_impares))



























