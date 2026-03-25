from pathlib import Path
import json

'''numero_favorito2 = input(f'Por favor, ingrese su número favorito: ')

path = Path('numero_favorito.json')
contenido_numero = json.dumps(numero_favorito2)
path.write_text(contenido_numero)

print(f'Recordaré tu número favorito.')

path = Path('numero_favorito.json')
contenido_numero = path.read_text()
numero_fav = json.loads(contenido_numero)

print(f'Tu número favorito es: {numero_fav}')'''


def recordar_numero_favorito():
    path = Path('numero_favorito.json')

    if path.exists():
        contenido_numero = path.read_text()
        numero_fav = json.loads(contenido_numero)
        print(f'Hola de nuevo. Tu número favorito es: {numero_fav}')
    else:
        numero_favorito_nuevo = input(f'Por favor, ingresa tu número favorito:')
        contenido_numero = json.dumps(numero_favorito_nuevo)
        path.write_text(contenido_numero)
        print(f'Gracias, recordaré tu número favorito')

print(f'Primera ejecución.')
recordar_numero_favorito()
print(f'Segunda ejecución.')
recordar_numero_favorito()















































































