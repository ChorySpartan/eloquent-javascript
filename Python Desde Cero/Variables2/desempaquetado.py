#DESEMPAQUETADOS

#Creando los datos

datos_en_tupla = ('Rodolfo', 'Laynez', 10)
datos_en_lista = ['Alejandro', 'Mota']

nombre, apellido, suscriptores = datos_en_tupla

#print(nombre, apellido)

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Rodolfo", edad=23, profesion="QA")
