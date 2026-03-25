#list // lista

#En esta si se pueden modificar los valores y van entre llaves
lista = ["Rodolfo", "Laynez", True, 1.85]

#Con la tupla // tuple NO se pueden modificar los valores y van entre paréntesis, y no entre llaves
tupla = ("Rodolfo", "Laynez", True, 1.85)

lista[3] = "Máquina" #Acá se usa la llave para modificar la lista

print(lista[3])

#Conjuntos // set

conjunto = {"Rodolfo", "Laynez", True, 1.85}

#conjunto[3] = "No se pueden redefinir" es decir, que no se puede acceder al índice

conjunto = {"aca se redefine el valor del conjunto"}
print(conjunto)

#Diccionarios // dict  // Estos no pueden repetir sus valores, es decir la clave y están desordendos

diccionario = {
    'nombre' : "Rodolfo",
    'apellido' : "Rodolfo",
    'valor' : True,
    'altura' : 1.70
}
print(diccionario)
