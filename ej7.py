
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad
        
    def setTitular(self, titular):
        self.titular = titular
        
    def getTitular(self):
        return self.titular
    
    def getCantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.__cantidad}")
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            
            
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad           
  

# Se crea objeto de la Cuenta
cuenta1 = Cuenta("John Smith", 10000)
# Detalle de cuenta
cuenta1.mostrar()
# Deposito de dinero
cuenta1.ingresar(500)
print("El deposito se realizo con exito.")
cuenta1.mostrar()
# Retiro de dinero
cuenta1.retirar(200)
print("El retiro de dinero se realizo con exito")
# Se muestra nuevamente los detalles de la cuenta.
cuenta1.mostrar()



