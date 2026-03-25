from pathlib import Path

#ESCRIBIR EN UN ARCHIVO VACÍO

'''
    Podemos agregar un texto a un archivo vacío, con el metodo write().
    Sin embargo, debemos de verificar si el documento realmente existe, ya que en caso de que
    ya exista, cuando se ejecute el W mode, se borrará el contenido del documento y se sobreescribirá
    lo que agreguemos.

    El argumento 'w' significa write mode, 'a' es append mode y 'r' es read mode.
    El último argumento es 'r+' y este nos permite leer y escribir en el archivo.
    Si no se agrega el argumento, por default se abre el archivo en read mode.
'''

filename = 'write_message.txt'
numero = 1

with open(filename, 'w') as file_object:
    file_object.write('Hello World!')
    file_object.write(f'{numero}')


#ESCRIBIR VARIAS LÍNEAS

libro = 'Me gusta mucho programar.\n'
libro += 'Aunque a veces es un poco dificil.\n'
libro += 'Ojala aprenda pronto.\n'

ruta = Path('write_message.txt')
ruta.write_text(libro)


#Ejercicio 10.4

#nombre = input('Por favor, ingrese su nombre: ')

#guest = Path('guest.txt')
#guest.write_text(nombre)


#Ejercicio 10.5


print('Bienvenido al Libro de Visitas. Escribe "salir" en cualquier momento para terminar.')

with open(filename, 'a') as file_object:
    while True:
        name = input('\nPor favor, ingrese su nombre (o escriba "salir" para terminar): ')

        if name.lower().strip() == 'salir':
            break
        else:
            print(f'Hola, {name}\n')
            file_object.write(f'{name}\n')

print(f"\n¡Gracias por usar el libro de visitas! Los nombres se han guardado en '{filename}'.")

print('\nContenido actual del Libro de Visitas')
with open(filename, 'r') as file_object:
    contenido_libro = file_object.read()
    print(contenido_libro)



















































































