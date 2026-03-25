#Le pedimos al usuario que nos diga una frase (o varias frases)

frase = input('Dime una frase y te calculo cuánto tardarías si tuvieras que decirla: ')

#Creamos una lista con todas las palabras de la frase (estas se separan cada vez que haya un espacio en blanco)

print('------------------------------------------------------------')
palabras_separadas = frase.split()

#Usamos len() para ver la cantidad de elementos que hay en la lista

cantidad_de_palabras = len(palabras_separadas)

#En caso de que tarde más de un minuto en decirlo, le indicamos que pare un poco

if cantidad_de_palabras > 120:
    print('Para flaco, tampoco te pedí un testamento')

#Calculamos cuánto tardaría en decir las palabras y se lo decimos

print(f'dijiste {cantidad_de_palabras} palabras, y tardarías {cantidad_de_palabras / 2} segundos en decirlo')
print('------------------------------------------------------------')
print(f'Dalto lo diría en {cantidad_de_palabras * 0.7 } segundos')
print('------------------------------------------------------------')