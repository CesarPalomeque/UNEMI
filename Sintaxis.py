# num =20
# nombre= "cesar"
# print(num,type(num))
# print(nombre,type(nombre))

# def mensaje(msg):
#   print(msg)

# mensaje("Mi primer programa en Pyton")
# mensaje("Mi segundo mensaje en Pyton")

class Sintaxis:
    instancia=0
    #__init__Metodoconstructor  que se ejecuta cuando se instancia la clase cuyo objetivo es crear 
    # e inicializar los atributos de la clase. Self es un objeto que representa la clase creada 
    def __init__(self,dato=""):
          self.frase=dato # atributo de instancia 
          Sintaxis.instancia = Sintaxis.instancia+1
    
    def usoVariable(self):
        edad, _peso  =25, 70.5
        nombre = 'Emanuel Palomeque'
        Tipo_sexo = 'M'
        civil = True
    #tuplas = son colecciones de datos de cualquier tipo inmutables
        usuario=()
        usuario = ('peroo','13587','emacerofoskrik@gmail.com')
        # print(usuario[1],nombre[11])

    #usuario[3]= "milagro"
    #listas = [] colecciones mutables
        materias = ['Programacion web','PHP','poo']
        aux= materias[1]
        materias[0] = "Python" 
        materias.append("go")
        #print(materias,aux,materias[1])
        # # Diccionario = {} colecciones de objetos clave: valor tipo json
        docente = {}
        docente = { 'nombre':'Emanuel','edad':'25','Activo':True}
        edad= docente['edad']
        docente['edad'] =51
        docente['categoria'] ='simple'
        #print(docente, edad, docente['edad'])
        #print(usuario,usuario[0], usuario[1:2],usuario[-1])
        #print(nombre,nombre[0], nombre[0:1],nombre[-3])
        print(materias,materias[2:], materias[:1],materias[:],materias[-3])
        

        # #presentacion con format 
        # print("""Mi nombre es {}, tengo {} años, peso {} kilos""".format(nombre,edad,_peso)) 
 
    
  
# print("Sintaxis antes de instancia es: {}".format(Sintaxis.instancia))
ejer1 = Sintaxis() # Instancia la clase sintaxis y crea el obejo ejer1 (copia de clase)
# print("Sintaxis de ejer1 es: {}".format(Sintaxis.instancia))
# ejer2 = Sintaxis()
#print(ejer1.frase)
# print("Sintaxis de ejer2 es: {}".format(Sintaxis.instancia))
# print(ejer2.frase)

ejer1.usoVariable()