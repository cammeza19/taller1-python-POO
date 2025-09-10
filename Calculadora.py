class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 == 0:
            return "Error: No se puede dividir entre 0"
        return self.num1 / self.num2


class JuegoCalculadora:
    def iniciar(self):
        print("Bienvenido a la Calculadora Simple")
        print("Escribe 'salir' en cualquier momento para terminar.\n")

        while True:
            # Pedir primer número
            num1 = input("Primer número: ")
            if num1.lower() == "salir":
                print("Hasta luego.")
                break
            if not num1.replace("-", "").isdigit():
                print("Debes ingresar un número válido.\n")
                continue
            num1 = float(num1)

            # Pedir segundo número
            num2 = input("Segundo número: ")
            if num2.lower() == "salir":
                print("Hasta luego.")
                break
            if not num2.replace("-", "").isdigit():
                print("Debes ingresar un número válido.\n")
                continue
            num2 = float(num2)

            # Crear objeto calculadora
            calc = Calculadora(num1, num2)

            # Pedir operación
            operacion = input("Operación (+, -, *, /): ")

            if operacion == "+":
                print("Resultado:", calc.sumar())
            elif operacion == "-":
                print("Resultado:", calc.restar())
            elif operacion == "*":
                print("Resultado:", calc.multiplicar())
            elif operacion == "/":
                print("Resultado:", calc.dividir())
            else:
                print("Operación no válida.")

            print()  # salto de línea


# Zona principal
juego = JuegoCalculadora()
juego.iniciar()
