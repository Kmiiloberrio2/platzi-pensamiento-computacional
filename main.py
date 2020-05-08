import aproximacion
import busqueda_binaria
import enumeracion_exhaustiva


def switch_algoritm(argument):
    switcher = {
        1: busqueda_binaria.calculate_square_root,
        2: enumeracion_exhaustiva.calculate_square_root,
        3: aproximacion.calculate_square_root,
    }
    func = switcher.get(argument, lambda: 'Invalid Number')
    return func(int(input('Escoge un numero: ')))


def main():
    algoritm = int(input('''Que algoritmo deseas utilizar? 
                            1: busqueda_binaria,
                            2: enumeracion,
                            3: aproximacion
                            (Elije una opcion, presionando solo un numero): '''))
    switch_algoritm(algoritm)


if __name__ == '__main__':
    main()
