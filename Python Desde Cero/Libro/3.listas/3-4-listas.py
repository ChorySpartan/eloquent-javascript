# Listas

lista = ['Adriana', 'Maythe', 'Richy', 'Gato Bety']

print(lista)
print(f'El invitado {lista[2]} no podrá asistir a la fiesta')

mensaje1 = f'Hola {lista[0]} quiero mucho beso paloma'

del lista[2]
lista.insert(2, 'Bea')

print(f'la nueva invitada es {lista[2]}')
print(lista)

print('Hola invitados, les comento que encontré una mesa más grande')

lista.insert(1, 'Sonia')
lista.insert(2, 'Abel')
lista.append('Salva')
print(lista)

print('\n'.join([f'Hola, {nombre}!' for nombre in lista]))

print('Lamentablemente, solo dos personas podrán ingresar')

print(lista[0], 'No puedes pasar')
lista.pop(0)
print(lista)

print(lista[0], 'No puedes pasar')
lista.pop(0)
print(lista)

print(lista[0], 'No puedes pasar')
lista.pop(0)
print(lista)

print(lista[0], 'No puedes pasar')
lista.pop(0)
print(lista)

print(lista[0], 'No puedes pasar')
lista.pop(0)
print(lista)

print(lista[0], 'y', lista[1], 'ustedes sí podrán ingresar')

del lista[0:2]

print(lista)