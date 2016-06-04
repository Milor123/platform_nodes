class Estudiante:
    identificacion = 0
    nombres = ""
    apellidos = ""
    edad = ""

    def __init__(self,nombre):
        print 'hola mundo', nombre
        self.nombreparatodos = nombre
        self.saltar(nombre)


    def saltar(self, apellido):
        print 'saltando', self.nombreparatodos
        print 'apellido es:', apellido

Estudiante('marcela')
