import time
import random

def sistema_reservas():
    print("\n Bienvenido al sistema de reservas de asientos")
    capacidad = int(input("Ingrese la capacidad de la sala: "))
    asientos = [False] * capacidad

    while True:
        print(f"Asientos disponibles: {asientos.count(False)}")
        if all(asientos):
            print("La sala está llena. No hay más reservas disponibles.")
            break
        asiento = int(input(f"Seleccione un asiento (0 a {capacidad-1}): "))
        if asiento < 0 or asiento >= capacidad:
            print("Número de asiento inválido")
        elif asientos[asiento]:
            print("Ese asiento ya está ocupado.")
        else:
            asientos[asiento] = True
            print(f"Reserva exitosa en el asiento {asiento}.")

        seguir = input("¿Desea reservar otro asiento? (s/n): ").lower()
        if seguir != "s":
            break


def fizzbuzz():
    print("\nBienvenido al juego FizzBuzz")
    while True:
        try:
            num = int(input("Digite un número: "))
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

        seguir = input("¿Desea probar con otro número? (s/n): ").lower()
        if seguir != "s":
            break


def calculadora():
    print("\nBienvenido a la calculadora simple")
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            op = input("Ingrese la operación (+, -, *, /): ")

            if op == "+":
                print(f"Resultado: {a + b}")
            elif op == "-":
                print(f"Resultado: {a - b}")
            elif op == "*":
                print(f"Resultado: {a * b}")
            elif op == "/":
                if b != 0:
                    print(f"Resultado: {a / b}")
                else:
                    print("Error: División por cero")
            else:
                print("Operación inválida")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

        seguir = input("¿Desea hacer otro cálculo? (s/n): ").lower()
        if seguir != "s":
            break


def control_temperatura():
    print("\nControl de temperatura en invernadero")
    for _ in range(5):
        temp = random.randint(0, 40)
        print(f"Temperatura: {temp}°C", end=" → ")
        if temp < 10:
            print("Calefactor encendido")
        elif temp > 25:
            print("Ventilador encendido")
        else:
            print("Sistema inactivo")
        time.sleep(1)


def deteccion_intrusos():
    print("\nSistema de detección de intrusos")
    alarma_activa = True
    for _ in range(5):
        sensores = [random.choice([True, False]) for _ in range(3)]
        noche = random.choice([True, False])
        print(f"Sensores: {sensores}, Noche: {noche}")
        if alarma_activa and noche and sensores.count(True) >= 2:
            print("Alarma activada")
        else:
            print("Sin alarma")
        time.sleep(1)


def control_luces():
    print("\nControl automático de luces")
    for _ in range(5):
        noche = random.choice([True, False])
        movimiento = random.choice([True, False])
        print(f"Noche: {noche}, Movimiento: {movimiento}", end=" → ")
        if noche and movimiento:
            print("Luces encendidas")
        else:
            print("Luces apagadas")
        time.sleep(1)


def control_aire():
    print("\nControl de aire acondicionado")
    for _ in range(5):
        temp = random.randint(20, 40)
        humedad = random.randint(30, 80)
        print(f"Temp: {temp}°C, Humedad: {humedad}%", end=" → ")
        if (temp > 28 and humedad > 60) or temp > 30:
            print("AC encendido")
        else:
            print("AC apagado")
        time.sleep(1)


def control_acceso():
    print("\nControl de acceso a tienda")
    while True:
        try:
            tiene_membresia = input("¿Tiene membresía? (s/n): ").lower() == "s"
            horario = input("¿Está dentro del horario de atención? (s/n): ").lower() == "s"
            es_empleado = input("¿Es empleado? (s/n): ").lower() == "s"

            if (tiene_membresia and horario) or es_empleado:
                print("Acceso permitido")
            else:
                print("Acceso denegado")
        except ValueError:
            print("Entrada inválida.")

        seguir = input("¿Desea probar otro caso? (s/n): ").lower()
        if seguir != "s":
            break


def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Sistema de Reservas")
        print("2. Juego FizzBuzz")
        print("3. Calculadora Simple")
        print("4. Control de Temperatura")
        print("5. Detección de Intrusos")
        print("6. Control de Luces")
        print("7. Control de Aire Acondicionado")
        print("8. Control de Acceso a Tienda")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema_reservas()
        elif opcion == "2":
            fizzbuzz()
        elif opcion == "3":
            calculadora()
        elif opcion == "4":
            control_temperatura()
        elif opcion == "5":
            deteccion_intrusos()
        elif opcion == "6":
            control_luces()
        elif opcion == "7":
            control_aire()
        elif opcion == "8":
            control_acceso()
        elif opcion == "9":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar menú
menu()
