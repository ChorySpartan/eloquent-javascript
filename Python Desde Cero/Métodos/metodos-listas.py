#Creando una lista con list()

lista = list([1, 2, 3, 4])

#Len devuelve la cantidad de elementos de una lista

cantidad_elementos = len(lista)

#Append agrega un elemento a la lista después del último elemento

agregando_con_append = lista.append(5) #"Elemento con Append el cual va de último"

#Insert agrega un elemento a la lista pero nosotros específicamos en qué índice

lista.insert(2, 6) #"Elemento insertado en el índice 2 con Insert"

#Extend agrega varios elementos a la lista

lista.extend([7]) #Extend que también se posiciona después del último índice"

#Pop elimina un elemento de una lista, en el índice que le indiquemos y devuelve un valor

lista.pop(0) #Este eliminó el número 1 y si queremos eliminar el último, debemos de agregar -1 en el parámetro
#Escribimos -2 para eliminar el ante último y así sucesivamente


#Remove remueve un elemento de una lista, y solicita un valor

#lista.remove() #Este muestra una excepción si no se agrega un parámetro existente


#Clear elimina todos los elementos de una lista

#list.clear()


#Sort ordena una lista de forma ascendente a descendente, sirve para ordenar la lista rápidamente

lista.sort(reverse=True) #Si le agregamos el parámetro reverse invierte el orden

#Reverse invierte los elementos de una lista

lista.reverse()

#Index verifica si un elemento se encuentra en la lista y nos indica el índice en donde se encuentra
#Sin embargo, nos mostrará solo el primer índice en caso de que se repita el elemento

elemento_encontrado = lista.index(2)

print(lista)