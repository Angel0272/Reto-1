# Importamos la biblioteca random para generar números aleatorios
import random

# Clase del juego
class AdivinaNumero:

    # Constructor
    def __init__(self):

        # Genera un número aleatorio entre 1 y 100
        self.numeroSecreto = random.randint(1,100)

        # Inicializa el contador de intentos
        self.intentos = 0

        # Define el máximo de intentos permitidos
        self.maxIntentos = 10

    # Método principal del juego
    def Jugar(self):

        print("================================")
        print("    JUEGO ADIVINA EL NUMERO   ")
        print("================================")
        print("He pensado un numero entre 1 y 100")
        print(f"Tienes {self.maxIntentos} intentos para adivinarlo")

        # Ciclo que se ejecuta mientras existan intentos disponibles
        while self.intentos < self.maxIntentos:

            # Solicita un número al usuario
            numero = int(input("Ingresa un numero: "))

            # Verifica que el número esté dentro del rango permitido
            if numero < 1 or numero > 100:

                print("Debes ingresar un numero entre 1 y 100")

            else:

                # Aumenta el contador de intentos
                self.intentos = self.intentos + 1

                # Verifica si el usuario adivinó el número
                if numero == self.numeroSecreto:

                    print("Felicidades, adivinaste el numero")
                    print(f"Lo lograste en {self.intentos} intentos")
                    break

                # Proporciona una pista si el número es menor
                elif numero < self.numeroSecreto:

                    print("El numero secreto es mayor")

                # Proporciona una pista si el número es mayor
                else:

                    print("El numero secreto es menor")

                # Muestra los intentos restantes
                print(f"Intentos restantes: {self.maxIntentos - self.intentos}")

        # Si el usuario no adivina el número en 10 intentos
        if self.intentos == self.maxIntentos and numero != self.numeroSecreto:

            print("Se acabaron los intentos")
            print(f"El numero secreto era {self.numeroSecreto}")

# Punto de entrada del programa
if __name__ == '__main__':

    # Crea un objeto de la clase
    juego = AdivinaNumero()

    # Ejecuta el juego
    juego.Jugar()
    #Ya termine el codigo
    #Se hicieron los cambios y cometarios