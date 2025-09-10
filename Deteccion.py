import random

class SistemaSeguridad:
    def __init__(self):
        self.sensores = [False, False, False]  # 3 sensores de movimiento
        self.noche = True                      # es de noche
        self.alarma_activa = False             # menú controla esto

    def leer_sensores(self):
        # Simulamos sensores (True = movimiento detectado, False = sin movimiento)
        self.sensores = [random.choice([True, False]) for _ in range(3)]

    def verificar_intrusion(self):
        if not self.alarma_activa:
            print("El sistema está desactivado. No se detectan intrusos.\n")
            return

        self.leer_sensores()
        print(f"Sensores: {self.sensores} | Noche: {self.noche}")

        if self.sensores.count(True) >= 2 and self.noche:
            print("ALARMA ACTIVADA: Intruso detectado!\n")
        else:
            print("Todo en orden, no hay intrusos.\n")

    def activar_alarma(self):
        self.alarma_activa = True
        print("Alarma ACTIVADA.\n")

    def desactivar_alarma(self):
        self.alarma_activa = False
        print("Alarma DESACTIVADA.\n")


class Menu:
    def iniciar(self):
        sistema = SistemaSeguridad()

        while True:
            print("=== Menú Sistema de Seguridad ===")
            print("1. Activar alarma")
            print("2. Desactivar alarma")
            print("3. Verificar sensores")
            print("4. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                sistema.activar_alarma()
            elif opcion == "2":
                sistema.desactivar_alarma()
            elif opcion == "3":
                sistema.verificar_intrusion()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intenta de nuevo.\n")


# Zona principal
menu = Menu()
menu.iniciar()
