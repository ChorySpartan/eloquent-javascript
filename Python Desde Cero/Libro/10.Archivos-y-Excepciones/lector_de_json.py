from pathlib import Path
import json

path = Path('numbers.json')
contenido = path.read_text()
numeros = json.loads(contenido)

print(numeros)






















