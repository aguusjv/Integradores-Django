class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print('La edad tiene que ser mayor de 0')

    def set_dni(self, dni):
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'DNI: {self.dni}')

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False   

p = Persona()
p.set_nombre('Juan')
p.set_edad(4)
p.set_dni('12345678A')  

p.mostrar() 
if p.es_mayor_de_edad():
    print('Es mayor de edad')
else:
    print('Es menor de edad') 