class viajes():

    def __init__(self):
        pass


    def usoFor(self):
     participantes=({'nombre':'cesar','edad':7},{'nombre':'merlina','edad':18},{'nombre':'Doris','edad':27},{'nombre':'jacniel','edad':14},{'nombre':'jacniel','edad':14},{'nombre':'jacniel','edad':14},{'nombre':'gabriela','edad':12})
     for pos,valor in enumerate(participantes):           
        #for clave,valor in participantes.items():
         print(pos,valor)
        #  lon = len(participantes)
        #  for pos in range(lon):
        #      if pos%2 == 0 and pos!=0:
        #        print(pos,participantes[pos]) 
               #print(pos,valor)
              
bucle= viajes()
bucle.usoFor()
