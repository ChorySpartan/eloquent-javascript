from funcion_1 import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('Janis', 'Joplin')
    assert formatted_name == 'Janis Joplin'

'''
    Debemos de nombrar las funciones con TEST al inicio y ser lo más descriptivos posible.
    
    Después se llama a la función que estará recibiendo el test.
    
    Por último con ASSERT se realiza una afirmación sobre una condición, en este caso que
    la función formatted_name tendrá que tener como resultado Janis Joplin.
'''







































































































