"""
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:

1.Agregar pasajeros a la lista de viajeros.
2.Agregar ciudades a la lista de ciudades.
3.Dado el DNI de un pasajero, ver a qué ciudad viaja.
4.Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
5.Dado el DNI de un pasajero, ver a qué país viaja.
6.Dado un país, mostrar cuántos pasajeros viajan a ese país.
7.Salir del programa.
"""


class Escuela:
    lista_alumnos = ['Luis', 'Francheska', 'Rosa']

    def ver_lista(self):
        print("\n\nLista de alumnos actuales: ", self.lista_alumnos)


def main():
    alumnus = Escuela()

    dict_information = {

        1: alumnus.ver_lista

    }

    while True:
        print("""
        1. Ver lista de estudiantes.    
        """)
        try:
            opcion = int(input("Ingrese option:\t"))
        except:
            print("Opcion Invalida")
            continue

        if opcion == 7:
            break

        dict_information[opcion]()


if __name__ == '__main__':
    main()
