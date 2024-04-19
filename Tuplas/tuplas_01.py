"""
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:

0. Salir del programa.
1. Ver lista de alumnos.
2. Agregar estudiante.
3. Eliminar estudiante.
4. Ver informacion de estudiante mediante ID.
5. Ver lista de materiales.
6. Ver calificaciones mediante ID.

"""


class Escuela:
    lista_alumnos = ['Luis', 'Francheska', 'Rosa']

    def ver_lista(self):
        print("\n\nLista de alumnos actuales: ", self.lista_alumnos)

    def agregar_estudiantes(self):
        name = input("Ingrese nombre: ")
        age = input("Ingrese edad: ")
        identification = input("Ingrese ID: ")
        student_information = (name, age, identification)
        self.lista_alumnos.append(student_information)

def main():
    alumnus = Escuela()

    dict_information = {

        1: alumnus.ver_lista,
        2: alumnus.agregar_estudiantes

    }

    while True:
        print("""
        0. Salir.
        1. Ver lista de estudiantes.
        2. Agregar estudiante.     
        """)
        try:
            opcion = int(input("Ingrese opcion:\t"))
        except:
            print("Opcion Invalida")
            continue

        if opcion == 0:
            print("Bye Bye")
            break

        dict_information[opcion]()


if __name__ == '__main__':
    main()
