class Biblioteca:

    # Constructor
    def __init__(self):

        # Lista donde se guardan los libros
        # Cada libro es un diccionario
        self.libros = []

    # Metodo para agregar libros
    def AgregarLibro(self):

        # Se piden los datos del libro
        titulo = input("Titulo del libro: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        copias = int(input("Numero de copias: "))

        # Se crea un diccionario para el libro
        libro = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "copias": copias
        }

        # Se agrega a la lista
        self.libros.append(libro)

        print("Libro agregado correctamente")

    # Metodo para buscar libros
    def BuscarLibro(self):

        print("\nBuscar por:")
        print("1. Titulo")
        print("2. Autor")
        print("3. Genero")

        opcion = int(input("Selecciona una opcion: "))

        encontrado = False

        if opcion == 1:

            titulo = input("Titulo a buscar: ")

            for libro in self.libros:

                if libro["titulo"].lower() == titulo.lower():

                    print(libro)
                    encontrado = True

        elif opcion == 2:

            autor = input("Autor a buscar: ")

            for libro in self.libros:

                if libro["autor"].lower() == autor.lower():

                    print(libro)
                    encontrado = True

        elif opcion == 3:

            genero = input("Genero a buscar: ")

            for libro in self.libros:

                if libro["genero"].lower() == genero.lower():

                    print(libro)
                    encontrado = True

        if encontrado == False:
            print("No se encontraron resultados")

    # Metodo para prestar libros
    def PrestarLibro(self):

        titulo = input("Titulo del libro a prestar: ")

        for libro in self.libros:

            if libro["titulo"].lower() == titulo.lower():

                if libro["copias"] > 0:

                    libro["copias"] = libro["copias"] - 1
                    print("Libro prestado correctamente")

                else:

                    print("No hay copias disponibles")

                return

        print("Libro no encontrado")

    # Metodo para devolver libros
    def DevolverLibro(self):

        titulo = input("Titulo del libro a devolver: ")

        for libro in self.libros:

            if libro["titulo"].lower() == titulo.lower():

                libro["copias"] = libro["copias"] + 1

                print("Libro devuelto correctamente")
                return

        print("Libro no pertenece al sistema")

    # Metodo para mostrar libros disponibles
    def MostrarLibros(self):

        print("\nLIBROS DISPONIBLES")

        for libro in self.libros:

            if libro["copias"] > 0:

                print("Titulo:", libro["titulo"])
                print("Autor:", libro["autor"])
                print("Genero:", libro["genero"])
                print("Copias:", libro["copias"])
                print("------------------------")

    # Menu principal
    def Menu(self):

        opcion = 0

        while opcion != 5:

            print("\n===== BIBLIOTECA =====")
            print("1. Agregar libro")
            print("2. Buscar libro")
            print("3. Prestar libro")
            print("4. Devolver libro")
            print("5. Salir")

            opcion = int(input("Selecciona una opcion: "))

            if opcion == 1:
                self.AgregarLibro()

            elif opcion == 2:
                self.BuscarLibro()

            elif opcion == 3:
                self.PrestarLibro()

            elif opcion == 4:
                self.DevolverLibro()

            elif opcion == 5:
                print("Saliendo del sistema")

            else:
                print("Opcion invalida")


# Ejecucion del programa
if __name__ == '__main__':

    sistema = Biblioteca()
    sistema.Menu()
    #Edite este codigo