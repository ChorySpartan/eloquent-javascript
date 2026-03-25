'''from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
    # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)'''

from pathlib import Path

def contar_alicia(archivopath):
    try:
        contenido3 = archivopath.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Lo siento, el archivo {archivopath.name} no existe.")
        return None
    else:
        palabras2 = contenido3.split()
        num_palabras = len(palabras2)
        print(f"El archivo {archivopath.name} tiene cerca de {num_palabras} palabras.")
        return contenido3

libro_alicia = 'alice.txt'
palabra_a_buscar = 'while'

ruta_alice2 = Path(libro_alicia)

contenido_alice = contar_alicia(ruta_alice2)
if contenido_alice:
    conteo_while = contenido_alice.lower().count(palabra_a_buscar.lower())
    print(f"La palabra '{palabra_a_buscar}' aparece {conteo_while} veces en '{libro_alicia}'")

print()

from pathlib import Path

def count_and_show_word_lines(filepath, word_to_find):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            line_number = 0
            found_count = 0
            found_lines = []

            for line in file:
                line_number += 1
                clean_line = line.lower().strip()

                if word_to_find.lower() in clean_line:
                    found_count += clean_line.count(word_to_find.lower())
                    found_lines.append(line_number)

    except FileNotFoundError:
        print(f"Sorry, the file {filepath.name} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading {filepath.name}: {e}")
    else:
        print(f"\n--- Resultados para '{word_to_find}' en '{filepath.name}' ---")
        if found_count > 0:
            print(f"La palabra '{word_to_find}' aparece {found_count} veces.")
            print("Aparece en las siguientes líneas:")
            print(found_lines)
        else:
            print(f"La palabra '{word_to_find}' no se encontró en el archivo.")

filename_alice = 'alice.txt'
palabra_a_buscar = 'while'

ruta_alice = Path(filename_alice)

count_and_show_word_lines(ruta_alice, palabra_a_buscar)



from pathlib import Path

def count_and_show_multiple_words_lines(filepath, words_to_find):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            line_number = 0
            results = {word.lower(): {'count': 0, 'lines': []} for word in words_to_find}

            for line in file:
                line_number += 1
                clean_line = line.lower().strip()

                for word in words_to_find:
                    word_lower = word.lower()
                    if word_lower in clean_line:
                        results[word_lower]['count'] += clean_line.count(word_lower)
                        if line_number not in results[word_lower]['lines']:
                            results[word_lower]['lines'].append(line_number)

    except FileNotFoundError:
        print(f"Sorry, the file {filepath.name} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading {filepath.name}: {e}")
    else:
        print(f"\n--- Resultados para '{filepath.name}' ---")
        found_any_word = False
        for word, data in results.items():
            if data['count'] > 0:
                found_any_word = True
                print(f"La palabra '{word}' aparece {data['count']} veces.")
                print(f"Aparece en las siguientes líneas: {data['lines']}")
            else:
                print(f"La palabra '{word}' no se encontró en el archivo.")

        if not found_any_word:
            print("Ninguna de las palabras buscadas fue encontrada en el archivo.")

filename_alice = 'alice.txt'
palabras_a_buscar = ['for', 'the', 'end']

ruta_alice = Path(filename_alice)

count_and_show_multiple_words_lines(ruta_alice, palabras_a_buscar)




from pathlib import Path
import collections
import re

def most_common_word(filepath):
    """
    Encuentra la palabra que más se repite en un archivo.
    Ignora mayúsculas/minúsculas y puntuación básica.
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filepath.name} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {filepath.name}: {e}")
        return None
    else:
        content_lower = content.lower()
        words = re.findall(r'\b\w+\b', content_lower)

        word_counts = collections.Counter(words)

        if word_counts:
            most_common = word_counts.most_common(1)
            word, count = most_common[0]
            print(f"\n--- Análisis de frecuencia para '{filepath.name}' ---")
            print(f"La palabra que más se repite es: '{word}' (aparece {count} veces).")
            # Si quieres ver las 10 más comunes, descomenta las siguientes líneas:
            # print("\nLas 10 palabras más comunes son:")
            # for w, c in word_counts.most_common(10):
            #     print(f"- '{w}': {c} veces")
            return word, count
        else:
            print(f"\nNo se encontraron palabras en el archivo '{filepath.name}'.")
            return None

# --- Código para analizar el libro de Alicia ---

filename_alice = 'alice.txt' # Asegúrate de que este archivo exista en la misma carpeta
ruta_alice = Path(filename_alice)

# Llamamos a la función para encontrar la palabra más común en 'alice.txt'
most_common_word(ruta_alice)

# --- FIN del código de análisis de Alicia ---

# Puedes eliminar o comentar el código de prueba con 'test_text.txt'
# si solo te interesa analizar 'alice.txt'