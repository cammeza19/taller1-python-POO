import time
import random

class AireAcondicionado:
    def __init__(self):
        self.temperatura = 25
        self.humedad = 50
        self.encendido = False

    def leer_sensores(self):
        # Simulación de sensores con valores aleatorios
        self.temperatura = random.randint(20, 40)   # entre 20 y 40 °C
        self.humedad = random.randint(30, 80)       # entre 30% y 80%

    def controlar_aire(self):
        if (self.temperatura > 28 and self.humedad > 60) or self.temperatura > 30:
            self.encendido = True
        else:
            self.encendido = False

    def mostrar_estado(self):
        estado = "Aire ENCENDIDO" if self.encendido else " Aire APAGADO"
        print(f"Temp: {self.temperatura}°C |  Humedad: {self.humedad}% → {estado}\n")


class SistemaClima:
    def iniciar(self):
        aire = AireAcondicionado()
        print("Sistema de Control de Aire Acondicionado iniciado...\n")
        print("Se verificará el estado cada 5 segundos. (Presiona Ctrl+C para detener)\n")

        while True:
            aire.leer_sensores()
            aire.controlar_aire()
            aire.mostrar_estado()
            time.sleep(5)  # espera 5 segundos antes de la siguiente lectura


#  Zona principal
clima = SistemaClima()
clima.iniciar()
