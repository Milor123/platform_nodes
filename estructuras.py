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
            pickle.dump(self.lista_estudiantes, self.myfile,-1)
            pickle.dump(self.lista_privado, self.myfile,-1)
            pickle.dump(self.lista_usuariofinal, self.myfile,-1)
            self.myfile.close()
    def archivo(self):
        """
        Este metodo se encarga de abrir o crear el archivo database en el que se almacenaran
        a los datos de los usuarios.
        """

        import os.path
        if os.path.isfile('database'):
            self.myfile = open('database','r+')
            self.lista_estudiantes = pickle.load(self.myfile)
            self.lista_privado = pickle.load(self.myfile)
            self.lista_usuariofinal = pickle.load(self.myfile)
            self.myfile.close()
            self.myfile = open('database','w')

        else:
            self.myfile = open('database','wb')

    def verificar(self):
        """
        Este metodo se encarga de validad que el usuario que va ingresar,
        no se encuentre registrado, esto se hace mediante el numero de identificacion
        """
        identificacion = self.E.identificacion
        for x in self.lista_estudiantes[:]:
            if identificacion in x.values():
                print ("El usuario ya esta repetido")
                self.flag_validar = False

    def generar_codigo(self):
        """
        Este metodo genera el codigo estudiantil apartir
        de los nombres, apellidos e identifiacion.
        """
        codigo = "{0}{1}{2}".format(self.E.nombres[:2],
                                  self.E.apellidos[:2],
                                  self.E.identificacion[:3])
        self.codigo = codigo

    def generar_usuario(self):
        """
        Este metodo se encarga de generar los usuarios
        apartir de su nombre, apellido y edad, generando
        un patron mas o menos random.
        """
        usuario = "{0}{1}{2}".format(self.E.nombres[0],
                               self.E.apellidos[:3],
                               self.E.edad)
        self.usuario = usuario

    def generar_password(self):
        """
        Este metodo se encarga de crear una contrasena para el
        usuario a travez de la identificacion y la edad.:update
        """
        password = "{0}_{1}".format(self.E.identificacion,
                                    self.E.edad)
        self.password = password

    def generar_dic(self):
        """
        Este metodo crea los diccionarios que posteriomente tendran la informacion
        de los usuarios.:update
        """

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
        """
        Este metodo introduce los diccinarios en las listas y luego los
        guarda en el archivo plano
        """

        self.lista_estudiantes.append(self.dic_estudiantes)
        self.lista_privado.append(self.dic_privado)
        pickle.dump(self.lista_estudiantes, self.myfile,-1)
        pickle.dump(self.lista_privado, self.myfile,-1)

    def crear_usuariofinal(self):
        """
        Este metodo se encarga de generar la lista_usuariofinal
        para esto adjunta el dia de la creacion y los diccionarios de los estudiantes
        y su informacion privada.
        """
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
        #import ipdb; ipdb.set_trace() # BREAKPOINT
        #self.lista_usuariofinal.insert(1,ultimo_dic_estudiantes)
        #TODO change insert
        pickle.dump(self.lista_usuariofinal, self.myfile,-1)
        self.myfile.close()

class Consultar:
    def __init__(self):
        """
        Este constructur se encarga de cargar los datos de database
        para que los metodos obtener, puedan devolver la informacion
        """
        self.myfile = open('database','r')
        self.lista_estudiantes = pickle.load(self.myfile)
        self.lista_privado = pickle.load(self.myfile)
        self.lista_usuariofinal = pickle.load(self.myfile)
        self.myfile.close()
    def obtener_estudiantes(self):
        """Este metodo devuelve la informacion de la lista_estudiantes"""
        return self.lista_estudiantes[:]

    def obtener_privado(self):
        """Igual que el anterior pero con la lista_privado"""
        return self.lista_privado[:]

    def obtener_usuarios(self):
        """Igual que el anteriror pero con la lista_usuariofinal"""
        return self.lista_usuariofinal[:]

class Modificar:
    def __init__(self):
        pass

    def abrir(self):
        """
        Este metodo carga los datos del archivo database y los deja
        abiertos, es decir quedan pendientes para ser sobreescritos con la ayuda
        del metodo cerrar()
        """

        self.myfile = open('database','r')
        self.lista_estudiantes = pickle.load(self.myfile)
        self.lista_privado = pickle.load(self.myfile)
        self.lista_usuariofinal = pickle.load(self.myfile)
        self.myfile.close()
        self.myfile = open('database','w')

    def cerrar(self):
        """
        Este metodo se encarga de guardar las variables en el archivo
        plano, que esta abierto y esperando gracias al metodo abrir()
        """

        pickle.dump(self.lista_estudiantes, self.myfile, -1)
        pickle.dump(self.lista_privado, self.myfile, -1)
        pickle.dump(self.lista_usuariofinal, self.myfile, -1)
        self.myfile.close()

    def modificar_estudiantes(self, dic, newdic):
        """
        Este metodo espera que pases un diccionario completo
        para luego ser sustituido por otro

        Ejemplo:
            modificar_estudiantes({'algo':'valor'},{'algo':'Nuevovalor'})
        """

        self.abrir()
        self.lista_estudiantes.modify(dic,newdic)
        self.cerrar()

    def modificar_privado(self, dic, newdic):
        """ Igual que el metodo anterior"""
        self.abrir()
        self.lista_privado.modify(dic,newdic)
        self.cerrar()
    def modificar_usuarios(self, dic, newdic):
        """Igual que el metodo anteior"""
        self.abrir()
        self.lista_usuariofinal.modify(dic,newdic)
        self.cerrar()

    def buscar(self,parametro): # 'key:value'
        """
        Este metodo espera que le envies un parametro del tipo
        llave: valor en un string, para que el busque y devuelva el diccinario
        si es que lo encontro.

        Deben coincidir mayusculas y minusculas

        Ejemplo:
            buscar('apellidos:bohorquez')

        """

        self.abrir()

        parametro = parametro.split(':')
        for number,x in enumerate(self.lista_usuariofinal[:]):
            for key,value in x.iteritems():
                if parametro[0] in key:
                    if parametro[1] in value:
                        self.cerrar()
                        self.posicion = number
                        self.valor_dictmp = x
                        print 'paso por aqui'
                        return x
        self.posicion = None
        print 'No se encontro el usuario'
        self.cerrar()

    def buscar_modificar(self,parametro, datonuevo): # 'key:value'
        """
        Este metodo modificar la lista_usuariofinal, haciendo
        una busqueda con un parametro y pasandole un dato nuevo

        Ejemplo:
            buscar_modificar('apellidos:bohorquez','nuevobohorquez')

        """
        nuevoparametro = parametro.split(':')
        from copy import deepcopy
        self.buscar(parametro) # esto es para sacar el self.valor_dictmp
        dic = deepcopy(self.valor_dictmp)
        dic[nuevoparametro[0]]= datonuevo
        self.abrir()
        self.lista_usuariofinal.modify(self.valor_dictmp, dic)
        self.cerrar()

    def eliminar_por_parametro(self,parametro):
        """
        Este metodo experiemntal, elimina todos los datos coincidentes
        al la busqueda, en otras palabras, si se elimina un apellido,
        el algoritmo eliminara todas los nodos relacinados con ese apellido.

        Advertencia:
            No se debe usar despues de haber usado insertar o haber cambiado el orden
            buscamente de las lista, tampoco habiando eliminado algo de forma individual

        Ejemplo:
            eliminar_por_parametro('apellidos:bohorquez')
            # Seran eliminados de las 3 listas, todos los datos relacionados
            con esa persona.

        """
        self.buscar(parametro) # esto es para sacar el self.posicion
        if self.posicion is not None:
        """
            self.abrir()
            self.lista_estudiantes.remove(self.posicion)
            self.lista_privado.remove(self.posicion)
            self.lista_usuariofinal.remove(self.posicion)
            self.cerrar()
        else:
            print 'Lo que usted quiere eliminar no existe'





Estudiante('Juma','Gapacho','888654','15451')
Estudiante('Juma','Gapacho','777888654','15451')
import ipdb; ipdb.set_trace() # BREAKPOINT
#Estudiante('iiiiiiiiiJuma','aaaaaaGapacho','44232777888654','15451')
