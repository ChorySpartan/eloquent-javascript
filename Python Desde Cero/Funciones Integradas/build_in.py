#FUNCIONES INTEGRADAS

#Encontrando el número mayor de una lista

numeros = [1, 2, 3, 4, 5,]

numero_mas_alto = max(numeros)
print(numero_mas_alto)

numero_mas_bajo = min(numeros)
print(numero_mas_bajo)


#Redondeando a 6 decimales

numero = round(12.56789, 2) #Esto redondea hacia el número más alto, pero primero
                            #debemos de pasar el número y luego los decimales que deseamos obtener 12, 2
print(numero)


#La función BOOL() retorna FALSE si le indicamos como parámetro cero 0, si no le ponemos none o false
#o si lo dejamos vacía ()

resultado_bool = bool(0)
print(resultado_bool)


#La función ALL comprueba los iterabables y si todos son TRUE retornará TRUE
#Es decir, que no le pongamos un FALSE, NONE, CERO 0

resultado_all = all({2, 'false'})
print(resultado_all)


#La función SUM() suma todos los valores iterables dentro de un código pero sólo funciona con números

sum_total = sum(numeros)
print(sum_total)















































