class Tarea:

    def __init__(self):
        pass
    def calcularJornada(self):

        ht, he, het= 0,0,0
        ph, phe, pt= 0,0,0

        ht = int(input("Ingrese horas trabajadas: "))
        ph = float(input("Ingrese valor hora: "))

        if ht > 40:
            he = ht-40
            if he > 8:
                het = he - 8
                ph8 = 8*ph*2
                phe = het*ph*3
            else:
                phe = 0
                ph8 = he*ph*2    
            pt = 40*ph + ph8 + phe
        else:
            ph8=0
            pt = ht*ph
        print("Sobretiempo<8:{}, Sobretiempo>8:{}, Jornada:{}".format(ph8,phe,pt))



tarea=Tarea()
tarea.calcularJornada()