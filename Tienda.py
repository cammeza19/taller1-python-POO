import time
import random

class ControlAcceso:
    def __init__(self):
        self.tiene_membresia = False
        self.horario_valido = True
        self.es_empleado = False

    def leer_datos(self):
        # Simulación aleatoria de clientes
        self.tiene_membresia = random.choice([True, False])
        self.horario_valido = random.choice([True, False])
        self.es_empleado = random.choice([True, False])

    def verificar_acceso(self):
        if (self.tiene_membresia and self.horario_valido) or self.es_empleado:
            return True
        else:
            return False

    def mostrar_estado(self):
        acceso = "Acceso PERMITIDO" if self.verificar_acceso() else " Acceso DENEGADO"
        print(f"Membresía: {self.tiene_membresia} | Horario válido: {self.horario_valido} | Empleado: {self.es_empleado} → {acceso}\n")


class SistemaTienda:
    def iniciar(self):
        acceso = ControlAcceso()
        print("Sistema de Control de Acceso a la Tienda iniciado...\n")
        print("Se verificará cada 5 segundos. (Presiona Ctrl+C para detener)\n")

        while True:
            acceso.leer_datos()
            acceso.mostrar_estado()
            time.sleep(5)  # espera 5 segundos antes de la siguiente persona


# Zona principal
sistema = SistemaTienda()
sistema.iniciar()
