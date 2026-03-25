#Partes de una lista

#Con esto podemos llamar a una parte de una lista, se le agrega un índice [0:3] para llamar a los primeros 3
jugadores = ['Charles', 'Javier', 'Pelón', 'Gaby', 'Esther']
print(jugadores[-3:])

#Podemos agregar solo [3:] para que nos muestre el tercer índice hasta el último

#También funciona al revés con [:4] esto nos muestra del índice cero al tercero

#Y también sirve con [-1] que nos muestra el último

#O bien podemos usar [-3:] para que nos muestre los últimos tres elementos de la lista

jugadores2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(jugadores2[::-1])

#El [::2] indica que inicie en el indice cero y que salte de dos en dos, por lo que nos muestra
# [1, 3, 5, 7, 9]

#Si ponemos [1:3] le estamos indicando que vaya del índice 1 al 2, que sería 2, 3

#Al usar [1::3] mostrará 2, 5, 8 ya que inicia en el índice 1 y recorre todito saltando de 3 en 3

#Por último al usar [::-1] nos devuelve la lista al revés



print('-------------------------------------------------------')


#Recorriendo un segmento


jugadores3 = ['Javi', 'Leyla', 'Misterio', 'Pancho', 'Luis']
print('Aquí están los primeros tres jugadores de mi equipo: \n')
for jugador in jugadores[:3]:
    print(jugador.title())


print('-------------------------------------------------------')

#Copiar una lista

mis_alimentos = ['Pizza', 'Tacos', 'Hamburguesas', 'Pollo', 'Carne']
comidas_de_mi_amigo = mis_alimentos[1:3]

#Con esto podemos agregar más cosas a la lista
mis_alimentos.append('Conejo')
comidas_de_mi_amigo.append('Cangrejo')

print('Mis comidas favoritas son: \n')
for comida in mis_alimentos:
    print(f'{comida}')

print('\nlas comidas favoritas de mi amigo son: \n')
for comida in comidas_de_mi_amigo:
    print(f'{comida}')

















