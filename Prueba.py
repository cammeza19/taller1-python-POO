class Saludo:
    #metodo constructor
    #se usa para inicializar objetos
    def __init__(self, dato_texto):
        self.mensaje = dato_texto
        print(self.mensaje)

    def get_mensaje(self):
        return self.mensaje
    
    def set_atributo(self, dato_nuevo_mensaje):
        self.mensaje = dato_nuevo_mensaje

    def toma_nombre(self):
        nombre_usuario = input("Nombre de usuario: ")
        return nombre_usuario


    def hacer_mensaje(self, dato_usuario):
        self.mensaje = "Hola " + dato_usuario
        self.imprimir_mensaje(self.mensaje)

    #cuando voy a usar un método de mi clase dentro de otro método de la misma clase debo usar self
    def imprimir_mensaje(self, dato_mensaje):
        print(dato_mensaje)

        


# **** código principal ****

texto = "Hola usuario"
objeto_mensaje = Saludo(texto)
nombre = objeto_mensaje.toma_nombre()
objeto_mensaje.hacer_mensaje(nombre)




