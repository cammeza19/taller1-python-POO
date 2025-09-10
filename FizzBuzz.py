class FizzBuzz:
    def verificar_numero(self, numero):
        if numero % 3 == 0 and numero % 5 == 0:
            return "FizzBuzz"
        elif numero % 3 == 0:
            return "Fizz"
        elif numero % 5 == 0:
            return "Buzz"
        else:
            return str(numero)


class JuegoFizzBuzz:
    def __init__(self):
        self.juego = FizzBuzz()

    def iniciar(self):
        print("Bienvenido al juego FizzBuzz")
        print("Ingresa un número entre 0 y 100 (o escribe 'salir' para terminar).")
        
        while True:
            entrada = input("Número: ")

            # Opción para salir
            if entrada.lower() == "salir":
                print("Gracias por jugar FizzBuzz.")
                break

            # Validar si la entrada es un número
            if not entrada.isdigit():
                print("Debes ingresar un número válido.")
                continue

            numero = int(entrada)

            # Validación de rango
            if numero < 0:
                print("El número no puede ser menor que 0.\n")
                continue
            if numero > 100:
                print("El número no puede ser mayor que 100.\n")
                continue

            # Si pasa todas las validaciones, evalúa el FizzBuzz
            resultado = self.juego.verificar_numero(numero)
            print(f"Resultado: {resultado}\n")


# Zona principal
juego = JuegoFizzBuzz()
juego.iniciar()
