#EXCEPCIONES
from pathlib import Path



print()

'''
    Las excepciones se manejan con bloques try-except. Estos le preguntan a Python para hacer
    algo, pero también le dice a Python qué hacer si se genera una excepción.
'''


#MANEJO DE LA EXCEPCIÓN ZeroDivisionError

'print(5/0)'

#USANDO BLOQUES try-except

#Si el código funciona dentro del try, el except es ignorado, de lo contrario mostrará
#lo que hayamos asignado.
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")



#USANDO else EN UN try-except

# El único código que debería ir en un bloque try es el código que podría provocar que se
# genere una excepción.

# El código adicional que debería ejecutarse sólo si el bloque de prueba fue exitoso;
# este código va en el bloque else.

'''
    El error ocurre en la línea que realiza la división, así que ahí es donde colocaremos 
    el bloque try-except.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
        
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
        
    else: 
        print(answer)'''



#MANEJO DE LA EXCEPCIÓN FileNotFoundError

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contenido = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist!.")


path = Path('horacio.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass
    #print(f"Sorry, the file {path} does not exist!.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} contains {num_words} words.")


#TRABAJAR CON MÚLTIPLES ARCHIVOS

#Podemos llamar a varios archivos a la vez, y con el except si alguno no existe simplemente
#se mostrará un mensaje al usuario

'''
    from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
    # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
'''


#ERROR SILENCIOSO

'''
    Con PASS después del EXCEPT podemos simplemente pasar el error y no mostrarle nada
    al usuario, es decir, que el usuario nunca va a saber que existió algún error al 
    ejecutar el programa. 
'''


#Ejercicio 10.6 y 10.7

'''
try:
    num1_str = input("\nFirst number: ")
    num1 = int(num1_str)
    num2_str = input("\nSecond number: ")
    num2 = int(num2_str)

    suma = num1 + num2
    print(f'La suma de {num1} y {num2} es {suma}')

except ValueError:
    print('Error. Por favor, ingrese únicamente dígitos numéricos')
'''

while True:
    try:
        num1_str = input("\nPrimer número (o escriba 'q' para salir): ")
        if num1_str.lower().strip() == 'q':
            break
        num2_str = input("\nSegundo número (o escriba 'q' para salir): ")
        if num2_str.lower().strip() == 'q':
            break

        num1 = int(num1_str)
        num2 = int(num2_str)

        suma = num1 + num2
        print(f'La suma de {num1} y {num2} es {suma}')

    except ValueError:
        print("Error. Por favor, escriba únicamente números. ")

print()



#Ejercicio 10.8 y 10.9

from pathlib import Path

def count_words(path):

    try:
        contenido2 = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        '''print(f"Sorry, the file {path.name} does not exist.")'''
        pass
    else:
        palabras = contenido2.split()
        num_palabras = len(palabras)
        print(f"The file {path.name} has about {num_palabras} words.")


docs = ['cats.txt', 'dogs.txt', 'moby_dick.txt']
for filename in docs:
    archivo = Path(filename)
    count_words(archivo)


#Ejercicio 10.10

from pathlib import Path

def contar_alicia(archivopath):
    try:
        contenido3 = archivopath.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Lo siento, el archivo {archivopath.name} no existe.")
        return None
    else:
        palabras2 = contenido3.split()
        num_palabras = len(palabras2)
        print(f"El archivo {archivopath.name} tiene cerca de {num_palabras} palabras.")
        return contenido3

libro_alicia = 'alice.txt'
palabra_a_buscar = 'while'

ruta_alice2 = Path(libro_alicia)

contenido_alice = contar_alicia(ruta_alice2)
if contenido_alice:
    conteo_while = contenido_alice.lower().count(palabra_a_buscar.lower())
    print(f"La palabra '{palabra_a_buscar}' aparece {conteo_while} veces en '{libro_alicia}'")

print()














































































