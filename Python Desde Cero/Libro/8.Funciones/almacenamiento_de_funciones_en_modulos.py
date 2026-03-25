#IMPORTANDO UN MÓDULO COMPLETO

#Primero debemos de escribir IMPORT y después, el módulo, es decir, el nombre del archivo que contiene
#las funciones que deseamos importar y utilizar.

#Cualquier función definida en el módulo estará disponible en el archivo en el que se importe
import pizza

#Después debemos de escribir el nombre del archivo que vamos a utilizar y después de un punto
#se escribe el nombre de la función que queremos llamar, en este caso es pizza.make_pizza
pizza.make_pizza(16, 'jamón')

'''Todas las importaciones que hagamos, deben de ir al inicio siempre, acá por ser ejemplos
   no se realizaron al inicio.'''

#Esto llama a la siguiente función y la ejecuta sin volver a escribir todo el código

#def make_pizza(size, *toppings):
    #print(f"\nMaking a {size}-inch pizza with the following toppings:")
    #for topping in toppings:
        #print(f"- {topping}")

print('-------------------------------------------------------------------')



#Importación de Funciones Específicas

#La sintaxis de esto es; from module_name import function_name, function_1, function_2
#Acá, después de la primera función se pueden importar más, colocando una coma y el nombre de la función

from pizza import libro_favorito

libro_favorito('El Rinoceronte')    #En este caso, no se debe de usar el módulo seguido del punto,
                                    #basta con llamar a la variable directamente


# Debemos de agregar la siguiente línea de código para que la función no se ejecute siempre de arriba
#hacia abajo en cada módulo en donde la importemos

''' if __name__ == "__main__": '''

#Esto es porque Python ejecutará siempre la función en el nuevo módulo, mostrando primero lo que se le asignó
#en el módulo de origen, y esto afectará a nuestro programa, pero solo sí se tiene que dejar el argumento
#libro_favorito('Alicia en el país de las maravillas') <-----------
#Esto es lo que afecta al ejecutarse, ya que mostraría primero esto, por ejemplo si se deja para mostrar
#un ejemplo de lo que se debe de agregar como argumento, si no, no es necesario

#La función debe de quedar así

''' def libro_favorito(titulo):
    print(f'Uno de mis libros favoritos es: {titulo}')
if __name__ == "__main__": <-----------------------------------------------
    libro_favorito('Alicia en el país de las maravillas') '''



#Usar AS para darle un alias a una función

from pizza import saludo2 as greet

greet('Javier')

'''def saludo2(username):    <--------------------- Acá no fue necesario el if name porque no tiene un argumento
    """Este es un saludo sencillo"""
    print(f'Hola, {username.title()}!')  <---------- saludo2('Rodolfo')   --- Esto es lo que iría abajo'''



#Usar AS para darle un alias a un módulo

# import pizza as p

#En este caso se debe de colocar después del nombre del módulo AS _NOMBRE DEL ALIAS_


#IMPORTAR TODAS las funciones en un módulo

#Sintaxis

'''from pizza import *'''


#FUNCIONES DE ESTILO

'''Debemos de nombrar las funciones, modulos y llamadas de estos con nombres lógicos y que puedan
   explicar o aclarar qué hacen, ya que será más fácil de ser utilizados por nosotros y por nuestros
   compañeros que lean el código.
   
   También es importante saber que para los valores predeterminados y para los argumentos clave, no 
   debemos de agregarle un espacio ni antes ni después del signo igual
   
   parámetro="valor predeterminado"   
   
   parámetro="valor" '''


#Ejercicio 8.15

from printing_functions import show_completed_models

diseno_nuevo = ['camisa', 'juguete']
disenos_completados = []

show_completed_models(diseno_nuevo)


'''Sintaxis'''


"""
    import module_name
    from module_name import function_name
    from module_name import function_name as fn
    import module_name as mn
    from module_name import *
"""

























































