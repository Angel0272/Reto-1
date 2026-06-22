# Clase que administra el inventario
class Inventario:

    # Constructor de la clase
    def __init__(self):

        # Lista de listas donde se almacenan los productos
        # Formato: [nombre, cantidad]
        self.productos = []

    # Metodo para agregar productos al inventario
    def AgregarProducto(self):

        # Solicita los datos del producto
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))

        # Variable para verificar si el producto existe
        encontrado = False

        # Recorre la lista de productos
        for producto in self.productos:

            # Compara el nombre ingresado con los existentes
            if producto[0].lower() == nombre.lower():

                # Si existe, aumenta la cantidad disponible
                producto[1] = producto[1] + cantidad

                encontrado = True

                print("Stock actualizado")
                break

        # Si no existe el producto, se agrega al inventario
        if encontrado == False:

            self.productos.append([nombre, cantidad])

            print("Producto agregado correctamente")

    # Metodo para mostrar todos los productos registrados
    def MostrarInventario(self):

        # Verifica si el inventario esta vacio
        if len(self.productos) == 0:

            print("El inventario esta vacio")

        else:

            print("\n===== INVENTARIO =====")

            # Recorre la lista de productos
            for producto in self.productos:

                print(f"Producto: {producto[0]}")
                print(f"Cantidad: {producto[1]}")
                print("----------------------")

    # Metodo para vender productos
    def VenderProducto(self):

        # Solicita el nombre del producto
        nombre = input("Nombre del producto a vender: ")

        # Variable para verificar si fue encontrado
        encontrado = False

        # Busca el producto en la lista
        for producto in self.productos:

            if producto[0].lower() == nombre.lower():

                encontrado = True

                # Si existe mas de una unidad
                if producto[1] > 1:

                    # Reduce una unidad del inventario
                    producto[1] = producto[1] - 1

                else:

                    # Si solo queda una unidad, elimina el producto
                    self.productos.remove(producto)

                print("Producto vendido correctamente")

                break

        # Mensaje si no se encontro el producto
        if encontrado == False:

            print("Producto no encontrado")

    # Metodo que muestra el menu principal
    def Menu(self):

        opcion = 0

        # El programa continua hasta seleccionar salir
        while opcion != 4:

            print("\n===== INVENTARIO BASICO =====")
            print("1. Agregar producto")
            print("2. Mostrar inventario")
            print("3. Vender producto")
            print("4. Salir")

            opcion = int(input("Seleccione una opcion: "))

            # Opcion para agregar producto
            if opcion == 1:

                self.AgregarProducto()

            # Opcion para mostrar inventario
            elif opcion == 2:

                self.MostrarInventario()

            # Opcion para vender producto
            elif opcion == 3:

                self.VenderProducto()

            # Opcion para salir
            elif opcion == 4:

                print("edita esta linea!!...")

            # Si la opcion no existe
            else:

                print("Opcion no valida")

# Punto de entrada principal del programa
if __name__ == '__main__':

    # Crea un objeto de la clase Inventario
    sistema = Inventario()

    # Ejecuta el menu principal
    sistema.Menu()