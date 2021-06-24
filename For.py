from typing import ForwardRef


class For:
    def __init__(self):
        pass
 

    def usoFor(self):
# ciclo repetitivo de incremento o decremento que se ejecuta por verdadero 
        nombre= 'Emanuelito'
        datos=["Emanuel" ,25, True]
        #poss    0         1    2
        numeros=(2,5.4,3,1,7)
        docente={'nombre':'Emanuel','edad':25,'facu':'faci'}
        listaNotas=[(30,40),(20,40),(50,40)]
        listaAlumnos=[{"nombre":"cesar","final":80},{"nombre":"rodolfo","final":56},{"nombre":"pancraseo","final":71}]

    # rango ([inicio=0], limite, [inc/dec=1]). genera un rango de valores desde un valor inicial a un valor final 
    # se ejecuta desde el inicio hasta el limite 
    # for con range() o for con colecciones
        # j=0
        # while j<5:
        #     print('while',j)
        #     j=j+1

        # for i in  range(5): #numero de rango (0,1,2,3,4)
        #     print('for',i,end="")

        # for i in  range(1,5): #numero de rango (1,2,3,4)
        #     print('for',i,end="")

        # for i in  range(2,10,2): #numero de rango (2,4,6,8)
        #     print('for',i,end="")     

        # for i in  range(12,3,-3): #numero de rango (12,9,6)
        #     print('for',i,end="")   

        # lon = len(datos)
        # for pos in range(lon):
        #     print(pos,datos[pos])  
        #     lon = len(numeros)
        # for pos in range(lon):
        #     print('posicion:',pos,'El numero es:',numeros[pos])
        # lon = len(nombre)
        # for pos in range(lon):
        #     if pos%2 == 0 and pos!=0:
        #        print(pos,nombre[pos])
        # lon = len(listaAlumnos)
        # for pos in range(lon):
        #     print(pos,listaAlumnos[pos])
        # lon = len(listaNotas)
        # for pos in range(lon):
        #     print(pos,listaNotas[pos])  
        
        #Vocal= ('a','e','i','o','u')
        # for elemen in nombre:
            
        #        print(elemen,end="")   
        # for elemen in datos:
            
        #        print(elemen,end="") 
        # lon = len(datos)
        # for pos in range(lon):
        #     print(pos,datos[pos])

        # for pos,valor in enumerate(datos):           
        #     print(pos,valor)

        for clave,valor in docente.items():           
            print(clave,valor)

bucle= For()
bucle.usoFor()
