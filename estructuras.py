class Estudiante(object):
    identificacion = 0
    nombres = ""
    apellidos = ""
    edad = ""

    def __init__(self, nombres, apellidos, identificacion, edad):
        self.nombres= nombres
        self.apellidos = apellidos
        self.identificacion = identificacion
        self.edad = edad
        Registrar(self)


class Registrar:

    def __init__(self, Estudiante_datos):
        self.E = Estudiante_datos
        self.generar_codigo()
        self.generar_password()
        self.generar_dic()

    def generar_codigo(self):
        codigo = "{0}{1}{2}".format(self.E.nombres[:2],
                                  self.E.apellidos[:2],
                                  self.E.identificacion[:3])
        self.codigo = codigo

    def generar_password(self):
        password = "{0}_{1}".format(self.E.identificacion,
                                    self.E.edad)
        self.password = password

    def generar_dic(self):

        # Diccionario de estudiantes
        dic_estudiantes = {'nombres':self.E.nombres,
                          'apellidos':self.E.apellidos,
                          'identificacion':self.E.identificacion,
                          'edad':self.E.edad}
        self.dic_estudiantes = dic_estudiantes

        # Diccionario de password

Estudiante('Juma','Gapacho','888654','15451')
