# CREANDO UNA FUNCIÓN SIMPLE CON def


def saludar():
    print('Esta es una función definida por el desarrollador')


# CREANDO UNA FUNCIÓN CON PARÁMETROS

def saludar2(nombre, sexo):
    sexo = sexo.lower()
    if sexo == 'mujer':
        adjetivo = 'reina'
    elif sexo == 'hombre':
        adjetivo = 'titan'
    else:
        adjetivo = 'amor'

    print(f'Hola {nombre}, mi {adjetivo} ¿Cómo andas?')

saludar2('Camila', 'Mujer')
saludar2('Rodolfo', 'Hombre')
saludar2('Cheje', 'No binario') #4.24.17



#CREAR UNA FUNCIÓN QUE NOS RETORNE VALORES

def crear_contrasena_random(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return contrasena, num

#Desempaquetando la función
password, primer_numero = crear_contrasena_random(3)

#Mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f'Tu contraseña nueva es: {password}')
print(f'El número utilizado para crearla fue: {primer_numero}')









































































