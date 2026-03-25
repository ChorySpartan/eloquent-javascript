#Faltó el profe y los pibes van a armar la clase

#Función para obtener al asistente y al profesor según la edad

def obtener_companeros(cantidad_de_companeros):

    #Creando la lista de los compañeros
    companeros = []

    #Ejecutando un for para pedir información de cada compañero
    for i in range(cantidad_de_companeros):
        nombre = input('Ingrese el nombre del compañero: ')
        edad = int(input('Ingrese la edad del compañero: '))
        companero = (nombre, edad)

        #Agregando la información a la lista
        companeros.append(companero)

    #Ordenándolos de menor a mayor según su edad
    companeros.sort(key = lambda x : x[1])


    #compañeros[x] devuelve una tupla con (nombre, edad) y después accede al nombre
    #para definir al asistente y al profesor
    asistente = companeros[0][0]
    profesor = companeros[-1][0]
    return asistente, profesor

asistente, profesor = obtener_companeros(5)

print(f'El profesor es: {profesor} y el asistente es: {asistente}')








































































































































