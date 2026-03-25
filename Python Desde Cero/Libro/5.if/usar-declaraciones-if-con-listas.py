#USAR DECLARACIONES if CON LISTAS

#COMPROBACIÓN DE UN VALOR EN LA LISTA

ingredientes = ['Hongos', 'Pimientos Verdes', 'Queso']
for ingrediente in ingredientes:
    if ingrediente == 'Pimientos Verdes':
        print('\nLo sentimos, no hay pimientos verdes para agregar a su orden')
    else:
        print(f'\nAgregando {ingrediente}')

print('\nSe termino de crear su orden ')


#COMPROBACIÓN DE QUE UNA LISTO NO ESTÉ VACÍA

ingredientes2 = []
if ingredientes2:
    for ingrediente in ingredientes2:
        print(f'Agregando {ingrediente}')
    print('\nSe termino de crear su orden')
else:
    print('\nEstás seguro de que quieres una pizza simple?')


#COMPROBACIÓN USANDO MÚLTIPLES LISTAS

ingredientes_disponibles = ['Lechuga', 'Carne', 'Tocino', 'Jamón', 'Pepinillos']
ingredientes_solicitados = ['Lechuga', 'Papas Fritas', 'Tocino']

for ingrediente_solicitado in ingredientes_solicitados:
    if ingrediente_solicitado in ingredientes_disponibles:
        print(f'\nAgregando {ingrediente_solicitado}')
    else:
        print(f'\nLo sentimos, no tenemos {ingrediente_solicitado}')

print('\nSe termino de crear su orden')














