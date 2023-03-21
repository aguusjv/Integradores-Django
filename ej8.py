from eje7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion
        
    def get_bonificacion(self):
        return self.bonificacion
        
    def es_titular_valido(self):
        edad = int(input("Por favor, ingrese su edad: "))
        if edad >= 18 and edad < 25:
            return True
        else:
            return False
        
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para hacer retiros.")
        
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("La Bonificación es %", self.bonificacion)

c = CuentaJoven("Juan Perez", 1000, 5)
c.mostrar() # Output: "Cuenta Joven\nBonificación: 5%"

