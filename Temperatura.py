class Invernadero:
    def __init__(self):
        self.temperatura = 0
        self.estado = "Inactivo"

    def controlar_temperatura(self):
        if self.temperatura < 10:
            self.estado = "Calefactor encendido"
        elif 10 <= self.temperatura <= 25:
            self.estado = "Sistema inactivo"
        else:
            self.estado = "Ventilador encendido"
        return self.estado

    def mostrar_estado(self):
        print(f"Temperatura actual: {self.temperatura}°C → {self.estado}\n")


class SistemaInvernadero:
    def iniciar(self):
        print("Sistema de Control de Temperatura del Invernadero\n")
        print("Ingresa la temperatura actual (o escribe 'salir' para terminar).\n")

        invernadero = Invernadero()

        while True:
            entrada = input("Temperatura: ")

            # salir del programa
            if entrada.lower() == "salir":
                print("Sistema finalizado.")
                break

            # validar que sea número
            if not entrada.replace("-", "").isdigit():
                print("Debes ingresar un número válido.\n")
                continue

            invernadero.temperatura = int(entrada)  # asignamos temperatura
            invernadero.controlar_temperatura()     # decide acción
            invernadero.mostrar_estado()            # imprime resultado


# Zona principal
sistema = SistemaInvernadero()
sistema.iniciar()
