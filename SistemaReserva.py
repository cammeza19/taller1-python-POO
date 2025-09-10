class Sala:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.ocupados = 0

    def asientos_disponibles(self):
        return self.capacidad - self.ocupados

    def reservar_asiento(self):
        if self.ocupados < self.capacidad:
            self.ocupados += 1
            return True  # Reserva exitosa
        else:
            return False  # Sala llena


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def reservar(self, sala):
        if sala.reservar_asiento():
            print(f" {self.nombre} ha reservado un asiento.")
        else:
            print(f" Lo sentimos {self.nombre}, no hay asientos disponibles.")


class SistemaReservas:
    def __init__(self, sala):
        self.sala = sala
        self.reservas = []   # lista de nombres que reservaron

    def iniciar(self):
        print("Bienvenido al sistema de reservas de cine")
        print(f"Capacidad total de la sala: {self.sala.capacidad} asientos\n")

        # Bucle para múltiples reservas
        while self.sala.asientos_disponibles() > 0:
            print(f"Asientos disponibles: {self.sala.asientos_disponibles()}")
            nombre = input("Ingresa tu nombre: ")
            usuario = Usuario(nombre)

            decision = input("¿Quieres reservar un asiento? (si/no): ").lower()
            if decision == "si":
                usuario.reservar(self.sala)
            elif decision == "no":
                print("Has decidido no reservar más asientos.")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        
        print("\nReservas finalizadas. La sala está llena o ya no hay más interesados.")


# Zona principal de ejecución
sala_cine = Sala(20)  # capacidad de la sala = 20 asientos
sistema = SistemaReservas(sala_cine)
sistema.iniciar()
