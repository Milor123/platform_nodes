import pickle

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

    lista_estudiante = []
    lista_privado = []
    lista_usuariofinal = []
    flag_validar = True

    def __init__(self, Estudiante_datos):
        self.flag_validar = True
        self.E = Estudiante_datos
        self.archivo()
        self.verificar()
        if self.flag_validar: # Verificar si la identifican no ha sido repetida
            self.generar_codigo()
            self.generar_usuario()
            self.generar_password()
            self.generar_dic()
            self.crear_listas()
            self.crear_usuariofinal()
            Consultar(self)

    def archivo(self):
        import os.path
        if os.path.isfile('database'):
            self.myfile = open('database','r')
            self.lista_estudiante = pickle.load(self.myfile)
            self.lista_privado = pickle.load(self.myfile)
            self.lista_usuariofinal = pickle.load(self.myfile)
        else:
            self.myfile = open('database','w')

    def verificar(self):
        identificacion = self.E.identificacion
        for x in self.lista_estudiante:
            if identificacion in x.values():
                import ipdb; ipdb.set_trace() # BREAKPOINT

                print ("El usuario ya esta repetido")
                self.flag_validar = False

    def generar_codigo(self):
        codigo = "{0}{1}{2}".format(self.E.nombres[:2],
                                  self.E.apellidos[:2],
                                  self.E.identificacion[:3])
        self.codigo = codigo

    def generar_usuario(self):
        usuario = "{0}{1}{2}".format(self.E.nombres[0],
                               self.E.apellidos[:3],
                               self.E.edad)
        self.usuario = usuario

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
        dic_privado = {'password':self.password,
                        'codigo' :self.codigo,
                       'usuario':self.usuario}
        self.dic_privado = dic_privado

    def crear_listas(self):
        self.lista_estudiante.append(self.dic_estudiantes)
        self.lista_privado.append(self.dic_privado)
        pickle.dump(self.lista_estudiante, self.myfile)
        pickle.dump(self.lista_privado, self.myfile)

    def crear_usuariofinal(self):
        from datetime import date
        ultimo_dic_estudiantes = self.lista_estudiante[-1]
        ultimo_dic_privado = self.lista_privado[-1]
        ultimo_dic_estudiantes.update(ultimo_dic_privado)

        fecha = date.today()
        fecha = "{0}/{1}/{2}".format(fecha.year,
                                     fecha.month,
                                     fecha.day)
        dic_fecha = {"fecha":fecha}
        ultimo_dic_estudiantes.update(dic_fecha) # agregar fecha el diccionario
        self.lista_usuariofinal.append(ultimo_dic_estudiantes)
        pickle.dump(self.lista_usuariofinal, self.myfile)

class Consultar:
    def __init__(self,obj):
        pass

    def obtener_estudiantes():
        pass

    def obtener_privado():
        pass

    def obtener_usuarios():
        pass

Estudiante('Juma','Gapacho','888654','15451')



