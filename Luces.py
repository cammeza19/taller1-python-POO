import time
import random

class SistemaLuces:
    def __init__(self):
        self.noche = True
        self.movimiento = False
        self.luces_encendidas = False

    def leer_sensores(self):
        # Simulamos los sensores
        self.movimiento = random.choice([True, False])
        self.noche = random.choice([True, False])

    def controlar_luces(self):
        if self.noche and self.movimiento:
            self.luces_encendidas = True
        else:
            self.luces_encendidas = False

    def mostrar_estado(self):
        estado = "Luces ENCENDIDAS" if self.luces_encendidas else "Luces APAGADAS"
        print(f"Noche: {self.noche} | Movimiento: {self.movimiento} → {estado}\n")


class SistemaDomotico:
    def iniciar(self):
        sistema = SistemaLuces()
        print("Sistema de Control Automático de Luces iniciado...\n")
        print("Se verificará el estado cada 10 segundos. (Presiona Ctrl+C para detener)\n")

        while True:
            sistema.leer_sensores()
            sistema.controlar_luces()
            sistema.mostrar_estado()
            time.sleep(10)  # espera 10 segundos


#Zona principal
domotica = SistemaDomotico()
domotica.iniciar()
