#SORT se usa para cambiar el orden de la lista de forma permanente

lista = ['a', 'z', 'k', 'l', 'u']

lista.sort()
print(lista)

#Si agregamos como parámetro REVERSE = TRUE la lista se ordenará de forma inversa
#lista.sort(reverse=True)
#print(lista)

#SORTED sirve para cambiar el orden de la lista de forma temporal y también se le puede agregar REVERSE

lista2 = sorted(lista, reverse = True)
print(lista2, len(lista2))

lista.reverse()
print(len(lista2))

