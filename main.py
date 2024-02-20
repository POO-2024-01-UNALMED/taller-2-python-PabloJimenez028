

class Asiento:
    def __init__(self, precio, color,  registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor):
        listaColores = ["rojo","verde","amarillo","negro","blanco"]
        if nuevoColor in listaColores:
            self.color = nuevoColor
        else:
            print("Color Inválido")


class Auto:
    def __init__(self, modelo, precio, asiento, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asiento = asiento
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self, numeroasiento):
        
        return numeroasiento


    def verificarIntegridad(self, ):
        if (Asiento.registro == Motor.registro and  Auto.registro):
            print("Auto original")
        else:
            print("Las piezas no son originales")
     
        


class Motor:
    def __init__(self, numeoroCilindros, tipo, registro):
        self.numeoroCilindros = numeoroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, numero):
        self.registro = numero
    
    def asignarTipo (self, nuevotipo):
        listatipos = ["gasolina","electrico"]
        if nuevotipo in listatipos:
            self.tipo = nuevotipo
        else:
            print("tipo inválido")