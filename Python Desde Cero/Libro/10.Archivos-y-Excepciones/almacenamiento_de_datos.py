#ARCHIVOS JASON
from platform import java_ver

print()

'''
    El módulo json le permite convertir estructuras de datos simples de Python en cadenas con 
    formato JSON y luego cargar los datos de ese archivo la próxima vez que se ejecute el programa.
    
    JSON significa JavaScript Object Notation
'''

#USANDO json.dumps() Y json.loads()

'''
    La función json.dumps() toma un argumento, es decir, un dato que debe convertirse al formato
    JSON. La función devuelve una cadena, que luego podemos escribir en un archivo de datos.
'''


from pathlib import Path
import json

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

path = Path('numbers.json')         #Acá creamos el archivo
contenido = json.dumps(numeros)     #Con json.dumps() se garda el listado de números
path.write_text(contenido)          #Esto escribirá la información en el archivo




#GUARDAR Y LEER DATOS GENERADOS POR EL USUARIO

username = input("Cuál es tu nombre? ")

path = Path('username.json')
contenido2 = json.dumps(username)
path.write_text(contenido2)

print(f"Te recordaremos cuando regreses, {username}")


#función para saludar al usuario del cual, fue guardado su nombre

path = Path('username.json')            #Acá es lo mismo que lo anterior.
contenido2 = path.read_text()           #Con esto se lee el path, en vez de hacer el dump
username = json.loads(contenido2)       #Y con esto, se carga el contenido guardado y se asigna
                                        #a la variable username

print(f"Bienvenido de regreso, {username}")    #Esto es lo que muestra el saludo y el usuario guardado



#REFACTORIZACIÓN

'''
    La refactorización es un proceso en el desarrollo de software que consiste en reestructurar 
    el código existente sin cambiar su comportamiento externo. El objetivo principal de la 
    refactorización es mejorar la calidad interna del código para hacerlo más legible, mantenible, 
    eficiente y fácil de extender, sin introducir nuevas funcionalidades o corregir errores externos.
    
    Es dividir el código en una serie de funciones que tienen tareas específicas, esto hace el código
    más limpio, más fácil de entender y de ampliar. 
'''


'''

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None         #Siempre debemos de retornar un valor esperado o ninguno en una función


#En esta parte, separamos lo que escribimos anteriormente en el else, para que sea parte de
#una función nueva, que si bien hace lo mismo, es más fácil de entender y de editar
def get_new_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}")

greet_user()

'''


#Ejercicio 10.11

numero_favorito = input(f'Por favor, ingrese su número favorito: ')

path = Path('numero_favorito.json')
contenido_numero = json.dumps(numero_favorito)
path.write_text(contenido_numero)

print(f'Recordaré tu número favorito.')

path = Path('numero_favorito.json')
contenido_numero = path.read_text()
numero_fav = json.loads(contenido_numero)

print(f'Tu número favorito es: {numero_fav}')























































































