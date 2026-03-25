#Pasar un número arbitrario de argumentos a una función

#En este caso, se pasan todos los argumentos a la función con *
def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print(f'- {topping}')

make_pizza('Pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print('-------------------------------------------------------')


#Mezclando argumentos posicionales y arbitrarios

#En este caso también se pasa un sólo argumento posicional y los demás arbitrarios al final
#Siempre el parámetro que acepta un número arbitrario de argumentos debe de colocarse al final
#en la definición de la función
def make_pizza2(size, *toppings2):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping2 in toppings2:
        print(f"- {topping2}")

make_pizza2(16, 'pepperoni')
make_pizza2(12, 'mushrooms', 'green peppers', 'extra cheese')

print('-------------------------------------------------------')



#Uso de argumentos de palabras clave arbitrarios

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Albert', 'Einstein',
                             location = 'Princeton',
                             field = 'Physics',
                             year = 1980,)
print(user_profile)

print('-------------------------------------------------------')


#Ejercicio 8-12

def sandwich(*elementos):
    print('\nMaking a sandwich with the following elementos: ')
    for elemento in elementos:
        print(f'- {elemento}')

sandwich('Tomate', 'Jamón', 'Queso')
sandwich('Pan', 'Lechuga', 'Pollo')
sandwich('Jalea', 'Mantequilla de Maní')

print('-------------------------------------------------------')


#Ejercicio 8.13

user = build_profile('Rodolfo', 'Laynez',
                     location = 'Quiché',
                     field = 'Engineering',
                     year = 1993)

print(user)

print('-------------------------------------------------------')


#Ejercicio 8.14

def automoviles(fabricante, modelo, **caracteristicas):
    auto_info = {'fabricante': fabricante, 'modelo': modelo}
    for key, value in caracteristicas.items():
        auto_info[key] = value
    return auto_info

auto_info = automoviles('Subaru', 'Outback',
                        color = 'Azul',
                        rin = '32')

print(auto_info)

print('-----------------------------------------------------')


def auto(fabrica, model, **cosos):
    cosos['Fabricante'] = fabrica
    cosos['Modelo'] = model
    return cosos

autos = auto('Toyota', '2002',
                             location = 'Guatemala',
                             rin = '32',
                             color = 'azul',)
print(autos)

print('-------------------------------------------------------')






















































