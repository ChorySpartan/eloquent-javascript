from pathlib import Path
import json

def persona(path):
    if path.exists():
        contents2 = path.read_text(encoding='utf-8')
        datos_usuario = json.loads(contents2)
        return datos_usuario
    else:
        return None

def obtener_datos(path):
    nombre = input("Ingrese el nombre de usuario: ")
    edad = input("Ingrese su edad: ")
    ciudad = input("Ingrese su ciudad: ")
    profesion = input("Ingrese su profesion: ")

    datos_usuario = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad,
        "profesion": profesion
    }

    contents2 = json.dumps(datos_usuario, indent=4, ensure_ascii=False)
    path.write_text(contents2, encoding='utf-8')
    datos_usuario = persona(path)
    if datos_usuario:
        print()
        print(f'Bienvenido de nuevo, esto es lo que recordamos de ti: ')
        print()
        print(f"Nombre: {datos_usuario['nombre']}")
        print(f"Edad: {datos_usuario['edad']}")
        print(f"Ciudad: {datos_usuario['ciudad']}")
        print(f"Profesion: {datos_usuario['profesion']}")
    else:
        datos_usuario = persona(path)
        print(f"Gracias {datos_usuario['nombre']}. Guardaremos tus datos para la próxima vez.")

path = Path("usuario.json")
obtener_datos(path)
