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
    profesion = input("Ingrese su profesión: ")

    datos_usuario = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad,
        "profesion": profesion
    }

    contents2 = json.dumps(datos_usuario, indent=4, ensure_ascii=False)
    path.write_text(contents2, encoding='utf-8')
    return datos_usuario

def saludar_usuario():
    path = Path("usuario.json")
    datos_guardados = persona(path)

    if datos_guardados:
        print(f"Último usuario guardado: {datos_guardados['nombre']}")
        confirmar = input("¿Eres esta persona? (s/n): ").lower()

        if confirmar == 's':
            print()
            print(f"¡Bienvenido de nuevo, {datos_guardados['nombre']}! Estos son tus datos:")
            print()
            print(f"Nombre: {datos_guardados['nombre']}")
            print(f"Edad: {datos_guardados['edad']}")
            print(f"Ciudad: {datos_guardados['ciudad']}")
            print(f"Profesión: {datos_guardados['profesion']}")
        else:
            print("\nVamos a registrar tus nuevos datos.")
            nuevos_datos = obtener_datos(path)
            print(f"\nGracias, {nuevos_datos['nombre']}. Tus datos han sido actualizados.")
    else:
        print("No hay datos guardados. Vamos a comenzar.")
        nuevos_datos = obtener_datos(path)
        print(f"\nGracias, {nuevos_datos['nombre']}. Tus datos han sido guardados.")

# Llamada principal
saludar_usuario()
