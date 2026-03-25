from pathlib import Path
import json

'''def greet_user():

    path = Path('username.json')
    if path.exists():           #El metodo exists() permite verificar si un archivo existe y devuelve
                            #true en este caso, y de lo contrario devolverá false
        contenido = path.read_text()
        username = json.loads(contenido)
        print(f"Bienvenido de regreso, {username}")

    #Si no existe el archivo, el else se va a ejecutar y va a solicitar el nombre de usuario
    else:
        username = input("Cuál es tu nombre?")
        contenido = json.dumps(username)
        path.write_text(contenido)
        print(f"Te recordaremos cuando regreses, {username}")

greet_user()'''



#REFACTORIZACIÓN

'''def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None         #Siempre debemos de retornar un valor esperado o ninguno en una función
    
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
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}")

greet_user()'''




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
































































