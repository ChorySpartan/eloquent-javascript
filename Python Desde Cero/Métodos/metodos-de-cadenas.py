cadena1 = "Hola soy Rodolfo"
cadena2 = "Bienvenido máquina"

#Convierte el texto a mayúsculas
resultado1 = cadena1.upper()

#Convierte el texto a minúsculas
resultado2 = cadena1.lower()

#Primera letra en mayúscula
resultado3 = cadena2.capitalize()

#Metodo que encuentra el índice de la primera aparición y si no encuentra nada, devuelve -1
busqueda_find = cadena1.find("Hola") #Aquí devuelve cero 0 porque H está en el índice cero

#Buscamos una cadena dentro de otra cadena y funciona igual que FIND pero esta no devuelve -1 si no
#encuentra nada, simplemente muestra un error, siendo este una excepción

busqueda_index = cadena1.index("Hola")

#Si es numérico devuelve True, y si no devuelve False, incluso si es texto pero siempre que sean números
es_numerico = cadena1.isnumeric()

#Si es alfa numérico devolverá True, en caso contrario False
#Este no debe de tener caracteres especiales, como espacios o símbolos
es_alfa_numerico = cadena1.isalpha()

#Cuenta las coincidencias de una cadena, dentro de otra cadena, la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")

#Cuenta cuántos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verifica si una cadena empieza con otra cadena dada, si es así devuelve True
empieza_con = cadena1.startswith("H") #True

#Verifica si una cadena termina con otra cadena dada, si es así devuelve True
termina_con = cadena1.endswith("o") #True

#Reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("Hola", "Hello")

#Separa las cadenas con la cadena que le pasemos, y estas son separadas por coma en el texto inicial
cadena_separada = cadena1.split(",")

print(cadena_separada)




























