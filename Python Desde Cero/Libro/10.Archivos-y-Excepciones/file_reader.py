#Para abrir un documento de texto, debemos de escribir:
# with open('nombre del archivo) as file_object: y luego llamar con una variable al
# metodo read().



with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(f'{contents.rstrip()}\n')


#RUTAS DE ARCHIVOS RELATIVAS Y ABSOLUTAS

#Ruta Relativa

'''
     Una ruta de archivo relativa le dice a Python que busque una ubicación determinada relativa 
     al directorio donde está almacenado el archivo del programa que se está ejecutando actualmente.
     
     SINTAXIS:
     with open('text_files/filename.txt') as file_object:
'''

#Ruta Absoluta

'''
    Se le puede indicar a Python exactamente dónde está el archivo en tu computadora,
    independientemente de dónde esté almacenado el programa que se está ejecutando. Esta se utiliza cuando
    la ruta relativa no funciona correctamente. 
    
    SINTAXIS:
    file_path = '/home/rodolfo/other_files/text_files/filename.txt'
    with open(file_path) as file_object:
'''


#ACCEDIENDO A LAS LÍNEAS DE UN ARCHIVO

filename= 'pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()
    #Con splitlines() se agregará un salto de línea a cada línea de texto para leerla de una mejor manera
    lines = contents.splitlines()

for line in lines:
        print(f'{line}')
print()

with open(filename) as file_object:
    for line in file_object:
        #Si utilizamos rstrip() se eliminarán los saltos de línea automáticamente en cada parte del texto.
        print(f'{line.rstrip()}')
print()


#HACIENDO UNA LISTA DE LÍNEAS DESDE UN ARCHIVO

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(f'{line.rstrip()}')
print()

#TRABAJAR CON EL CONTENIDO DE UN ARCHIVO

'''
    Con esta función, podemos leer todo el contenido de un archivo, sin saltos de línea
    y además con len() cuenta cuantos caracteres tiene el archivo. 
'''
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
print()


#ARCHIVOS GRANDES

'''
    Si tenemos un archivo con un número que contenga demasiados datos, como un millón por ejemplo,
    podemos pasarle al programa una cantidad exacta de números que necesitamos con:
    
    print(f'{pi string[:52]}...') 
'''

print(pi_string[:12])
print(len(pi_string))
print()


#Ejercicio 10.1

with open('learning_python.txt') as file_object:
    contenido = file_object.read()
    print(contenido)
    print(len(contenido))
print()

print("Contenido del archivo almacenado en una lista y con un recorrido")

lineas = []
with open('learning_python.txt') as file_object:
    for linea in file_object:
        lineas.append(linea.strip())

for linea in lineas:
    print(linea)
print()



#Ejercicio 10.2

contenido_modificado = contenido.replace('Python', 'C').replace('python', 'C')
print(contenido_modificado)








































































