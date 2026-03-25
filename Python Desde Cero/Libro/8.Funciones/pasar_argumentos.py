#ARGUMENTOS POSICIONALES

def describir_mascota(tipo_de_mascota, nombre_mascota):
    #Esto muestra la información de la mascota
    print(f'\nTengo un {tipo_de_mascota}.')
    print(f'El nombre de mi {tipo_de_mascota} es {nombre_mascota.title()}.')

describir_mascota('Gato', 'Mochi')


#LLAMADAS A FUNCIONES MÚLTIPLES

describir_mascota('Gato', 'Bola de Nieve')
describir_mascota('Perro', 'Togo')
#Acá se llama varias veces a la misma función y muestra ambos resultados, se puede repetir este proceso
#cuantas veces sean requeridas por el programa que estemos realizando
#El orden de los argumentos es importante al usar estas funciones



#ARGUMENTOS DE PALABRAS CLAVE

def describir_mascota2(tipo, nombre):
    print(f'\nTengo un {tipo}.')
    print(f'El nombre de mi {tipo} es {nombre.title()}.')

describir_mascota2(tipo = 'Gato', nombre = 'Mochi')
describir_mascota2(nombre = 'Bola de Nieve', tipo = 'Gato')
#En este caso, no importa el orden ya que al usar keywords le asignamos el valor a cada argumento



#VALORES PREDETERMINADOS

def describir_mascotas4(nombre2, tipo2 = 'perro' ):
    print(f'\nTengo un {tipo2}.')
    print(f'El nombre de mi {tipo2} es {nombre2.title()}.')

describir_mascotas4(nombre2 = 'Togo')
#Esto se puede usar si no se tiene otro valor para una variable, por ejemplo al poner perro en tipo2
#se toma como un valor por defecto y siempre va a devolver perro como el valor de esa variable
describir_mascotas4(nombre2 = 'Mochi', tipo2 = 'Gato')
#Sin embargo, podemos cambiar el valor por defecto que colocamos por otro valor y se tomará
#este nuevo valor y el valor por defecto se ignorará



#LLAMADAS A FUNCIONES EQUIVALENTES

def describe_pet(pet_name, animal_type='dog'):
    print(f'\nTengo un {animal_type}.')
    print(f'El nombre de mi {animal_type} es {pet_name.title()}.')

# A dog named Willie.
describe_pet('willie')

describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')

describe_pet(pet_name='harry', animal_type='hamster')

describe_pet(animal_type='hamster', pet_name='harry')
#Asignamos un valor por defecto, pero cada llamada de la función es diferente, pero devuelve los
#mismos resultados, por eso son llamadas FUNCIONES EQUIVALENTES

print('----------------------------------------------------')


#Ejercicio 8.4

def make_shirt(talla, mensaje):

    print(f'\nTengo una camisa talla {talla} y el mensaje dice: {mensaje}.')

make_shirt('L', 'Hola nena, me dicen el Mike')
make_shirt(talla = 'M', mensaje = 'Ay mamasita')

print('----------------------------------------------------')

def camiseta_grande(talla2 = 'L', mensaje2 = 'Me encanta programar'):
    print(f'\nTengo una camisa talla {talla2} y el mensaje dice {mensaje2}.')

camiseta_grande()
camiseta_grande(talla2 = 'S', mensaje2 = 'Mensaje nuevo')

print('----------------------------------------------------')


#Ejercicio 8.5

def ciudad(nombre_ciudad, pais = 'Guatemala'):
    print(f'{nombre_ciudad} está en {pais}')

ciudad('Santa Cruz del Quiché')
ciudad('El Petén')

print('----------------------------------------------------')



























































