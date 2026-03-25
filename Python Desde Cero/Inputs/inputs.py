#INPUTS siempre devuelve un texto, incluso si se le ingresan números

#Pedirle un dato al usuario

nombre = input("Perro, dame tu nombre al tiro ctm: ")

#Convirtiendo un número que es texto a int (entero)

resultado = int(nombre) * 2 #Podemos poner FLOAT en lugar de INT o podemos poner BOOL

#Mostrando el dato

print(f'el nombre es: {nombre}')

print(resultado)