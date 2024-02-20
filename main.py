

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor:str):
        listaColores = ["rojo","verde","amarillo","negro","blanco"]
        if nuevoColor in listaColores:
            self.color = nuevoColor

class Auto:
    cantidadCreados = int
    def __init__(self, modelo, precio, asiento, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asiento = asiento
        self.marca = marca
        self.motor = motor
        self.registro = registro
        

    def cantidadAsientos(self):
        i = 0
        for asiento in self.asiento:
            if i != None and isinstance(i, Asiento):
                i += 1
        return i


    


    def verificarIntegridad(self):
        i = 0
        for i in self.asiento:
            if i != None:
                if i == self.registro and i == self.motor.registro:
                    verificacionasiento = True
                    
                else:
                    return "Las piezas no son originales"
            else:
                continue
        return "Auto original"





        
                
       


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




a1 = Asiento("blanco", 5000, 435)
a2 = Asiento("blanco", 5000, 435)
      
a1.cambiarColor("naranja")
a2.cambiarColor("verde")
print (a1.color,a2.color)