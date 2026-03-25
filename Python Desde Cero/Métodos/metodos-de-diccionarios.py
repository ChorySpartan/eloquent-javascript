diccionario = {
    "nombre" : "Rodolfo",
    "apellido" : "Laynez",
    "subs" : '10'
}

#KEYS os devuelve un objeto dict_item - Una lista de todas las claves junto con su valor

claves = diccionario.keys() # {'nombre': 'Rodolfo'}

#GET nos permite acceder a un valor, es decir, obtener un valor que queremos pero si no lo encuentra
#El programa puede continuar, en cambio si solicitamos el objeto con un índice el programa muestra un error

valor_de_get = diccionario.get("nombre")

#CLEAR elimina todo del diccionario

#clear = diccionario.clear()

#POP elimina un elemento del diccionario

#diccionario.pop("numero")

#ITEMS nos devuelve el diccionario, a diferencia del keys, este itera los elementos, es decir, los recorre
#Esto es lo que muestra
# diccionario_items ([('nombre', 'Rodolfo'), ('apellido': 'Laynez')])
diccionario_iterable = diccionario.items()

print(diccionario_iterable)