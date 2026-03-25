#Forma NO óptima de sumar valores

def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
resultado = suma([1, 2, 3, 4, 5, 6])

print(resultado)



#Forma ÓPTIMA de sumar valores con ARGS *

def suma2(nombre, *numeros):
    return f'{nombre}, la suma de tus números es: {sum(numeros)}'

resultado2 = suma2('Rodolfo',1, 2, 3, 4, 5, 6,)
print(resultado2)










































