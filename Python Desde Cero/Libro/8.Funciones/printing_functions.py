def imprimir(unprinted, acdc):
    while unprinted:
        current_design2 = unprinted.pop()
        print(f'Printing model: {current_design2}')
        acdc.append(current_design2)

def show_completed_models(acdc):
    print(f'\nThe following models have been printed:')
    for completed_model in acdc:
        print(completed_model)

if __name__ == "__main__":
    un = ['phone case', 'robot pendant', 'dodecahedron']
    ab = []
    imprimir(un, ab)
    show_completed_models(ab)


















































