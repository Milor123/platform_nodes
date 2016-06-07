import cPickle as pickle
from newlistas import LinkedList, Node

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

    lista_estudiantes = LinkedList()
    lista_privado = LinkedList()
    lista_usuariofinal = LinkedList()
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
        else:
            pickle.dump(self.lista_estudiantes, self.mylista_estudiantes,-1)
            pickle.dump(self.lista_privado, self.mylista_privado,-1)
            pickle.dump(self.lista_usuariofinal, self.mylista_usuariofinal,-1)
            self.mylista_estudiantes.close()
            self.mylista_privado.close()
            self.mylista_usuariofinal.close()
    def archivo(self):
        import os.path
        if os.path.isfile('lista_estudiantes'):
            self.mylista_estudiantes = open('lista_estudiantes','r')
            self.lista_estudiantes = pickle.load(self.mylista_estudiantes)
            self.mylista_estudiantes.close()

            self.mylista_privado = open('lista_privado','r')
            self.lista_privado = pickle.load(self.mylista_privado)
            self.mylista_privado.close()

            self.mylista_usuariofinal = open('lista_usuariofinal','r')
            self.lista_usuariofinal = pickle.load(self.mylista_usuariofinal)
            self.mylista_usuariofinal.close()

            self.mylista_estudiantes = open('lista_estudiantes','wb')
            self.mylista_privado = open('lista_privado','wb')
            self.mylista_usuariofinal = open('lista_usuariofinal','wb')
        else:
            self.mylista_estudiantes = open('lista_estudiantes','wb')
            self.mylista_privado = open('lista_privado','wb')
            self.mylista_usuariofinal = open('lista_usuariofinal','wb')

    def verificar(self):
        identificacion = self.E.identificacion
        for x in self.lista_estudiantes[:]:
            if identificacion in x.values():
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
        self.lista_estudiantes.append(self.dic_estudiantes)
        self.lista_privado.append(self.dic_privado)
        pickle.dump(self.lista_estudiantes, self.mylista_estudiantes,-1)
        self.mylista_estudiantes.close()
        pickle.dump(self.lista_privado, self.mylista_privado,-1)
        self.mylista_privado.close()

    def crear_usuariofinal(self):
        from datetime import date
        ultimo_dic_estudiantes = self.lista_estudiantes[-1][0]
        ultimo_dic_privado = self.lista_privado[-1][0]
        ultimo_dic_estudiantes.update(ultimo_dic_privado)

        fecha = date.today()
        fecha = "{0}/{1}/{2}".format(fecha.year,
                                     fecha.month,
                                     fecha.day)
        dic_fecha = {"fecha":fecha}
        ultimo_dic_estudiantes.update(dic_fecha) # agregar fecha el diccionario
        self.lista_usuariofinal.append(ultimo_dic_estudiantes)
        pickle.dump(self.lista_usuariofinal, self.mylista_usuariofinal,-1)
        self.mylista_usuariofinal.close()
class Consultar:
    def __init__(self):
        self.mylista_estudiantes = open('lista_estudiantes','rb')
        self.lista_estudiantes = pickle.load(self.mylista_estudiantes)
        self.mylista_estudiantes.close()

        self.mylista_privado = open('lista_privado','rb')
        self.lista_privado = pickle.load(self.mylista_privado)
        self.mylista_privado.close()

        self.mylista_usuariofinal = open('lista_usuariofinal','rb')
        self.lista_usuariofinal = pickle.load(self.mylista_usuariofinal)
        self.mylista_usuariofinal.close()

    def obtener_estudiantes(self):
        return self.lista_estudiantes[:]

    def obtener_privado(self):
        return self.lista_privado[:]

    def obtener_usuarios(self):
        return self.lista_usuariofinal[:]


Estudiante('Juma','Gapacho','888654','15451')
Estudiante('Juma','Gapacho','777888654','15451')
import ipdb; ipdb.set_trace() # BREAKPOINT

