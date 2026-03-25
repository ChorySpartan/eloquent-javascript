def saludo():
    """Este es un saludo sencillo"""
    print('Hola')

saludo()

print('------------------------------------')

def saludo2(username):
    """Este es un saludo sencillo"""
    print(f'Hola, {username.title()}!')

saludo2('Rodolfo')

print('------------------------------------')

#ARGUMENTOS Y PARÁMETROS

"""
Cuando tenemos una función cuando nombramos la variable se llama parámetro, por ejemplo,
def suma(parámetro) es lo que creamos dentro de la función

Cuando le pasamos la información a esa variable, eso se llama argumento
def suma('argumento') es lo que le asignamos a la variable creada    

"""

#Ejercicio 8.1

def saludo3(usuario):
    info = input('Por favor, ingrese su nombre: ')
    print(f'{usuario}, hola {info}')

saludo3('Primero que nada')

print('------------------------------------')

#Ejercicio 8.2

def libro_favorito(titulo):
    print(f'Uno de mis libros favoritos es: {titulo}')

libro_favorito('Alicia en el país de las maravillas')
























































