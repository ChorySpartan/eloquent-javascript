#DECLARACIÓN IF

autos = ['audi', 'bmw', 'ford', 'toyota', 'mazda', 'mitsubishi']
for autos in autos:
    if autos == 'bmw':
        print(autos.upper())
    else:
        print(autos.title())

print('\n------------------------------------------------------------ \n')
#La declaración = establece un valor y el doble igual == plantea si algo es exactamente igual
# a otra declaración

solicitud = 'Calabaza'

if solicitud != 'Jamón':
    print('¡Detén la orden!')

#COMPROBANDO MÚLTIPLES CONDICIONES CON AND Y OR

#AND

edad_1 = 22
edad_2 = 18
if edad_1 >= 21 and edad_2 <= 21: #esto se puede hacer más simplificado con
    # edad_1 >= 21 >= edad_2
    print('Hola soy Gokú')

#OR

edad_3 = 22
edad_4 = 18
if edad_3 >= 18 and edad_4 <= 18: #De nuevo esto se puede simplificar con
    # edad_3 >= 18 >= edad_4
    print('Vieja Tepta')

