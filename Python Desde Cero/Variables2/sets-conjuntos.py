#SET creando un conjunto con set()

conjunto = set(["Dato1"])

#FROZENSET permite meter un conjunto dentro de otro conjunto

conjunto1 = frozenset(["Dato1", "Dato2"])
conjunto2 = {conjunto1, "Dato 3"}

#print(conjunto2)

#Teoría de conjuntos

conjunto3 = {1, 2, 3, 4, 5}
conjunto4 = {1, 3, 5}

#Verificando si es un subconjunto
resultado = conjunto4.issubset(conjunto3)

#Esto es para ver si el conjunto 4 es un conjunto o subconjunto, en este caso es subconjunto
resultado2 = conjunto4 <= conjunto3

#Verificando si es un Súper Conjunto
resultado3 = conjunto4.issuperset(conjunto3)
resultado4 = conjunto4 > conjunto3

#Verificando si sólo existe un número en común entre los conjuntos
#Devolverá TRUE sólo si los conjuntos no poseen nada en común

resultado5 = conjunto2.isdisjoint(conjunto1) #En este caso muestra True porque no poseen nada en común

print(resultado5)