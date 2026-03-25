#Creando diccionarios con dict()

#Con estos si se pueden crear diccionarios vacíos a diferencia de la otra versión de los diccionarios
#que no pueden tener valores vacíos

diccionario = dict(nombre = 'Rodolfo', apellido = 'Laynez')

# diccionario {
#       'nombre': 'Rodolfo'
#       'apellido': 'Laynez'
#}

#FROMKEYS sirve para crear únicamente las claves en un diccionario y asigarle NONE por defecto a los valores

diccionario3 = dict.fromkeys(['Nombre', 'Apellido']) #Este fue creado con una lista []

claves = ['Nombre', 'Apellido']
diccionario4 = dict.fromkeys(claves) #Esta es otra forma de crear un diccionario sin valores 

print(diccionario4)