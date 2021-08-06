class Estructura_estatica:

    def __init__(self,lista):
        self.lista=lista
    
    def presentarLista(self):
        print('Recorrer y presentar los datos de una lista')
        for list in self.lista:
            print(list,end="   ")
        print('\n')
    
    def usoFor(self):
        participantes=({'nombre':'cesar','edad':7},{'nombre':'merlina','edad':18},{'nombre':'Doris','edad':27},{'nombre':'jacniel','edad':14},{'nombre':'jacniel','edad':14},{'nombre':'jacniel','edad':14},{'nombre':'gabriela','edad':12})
        for pos,valor in enumerate(participantes):           
        #for clave,valor in participantes.items():
         print("la posicion {} el elemento de la lista: {}  ".format(pos,valor) )
         #print(pos,valor)
        #  lon = len(participantes)
        #  for pos in range(lon):
        #      if pos%2 == 0 and pos!=0:
        #        print(pos,participantes[pos]) 
               #print(pos,valor)
    def buscarLista(self,buscado):
        print("busca un valor en una lista")
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:
           print("Su valor se encuentra en la lista, se encuentra en la posicion: {}".format(pos+1),"y es",ele)
           
        else:
            print('Su valor no se encuentra en esta lista')   


    


        
        


           

              
lista=[{'nombre':'cesar','edad':7},{'nombre':'Doris','edad':27},{'nombre':'jacniel','edad':14},{'nombre':'jacniel','edad':14},{'nombre':'gabriela','edad':12}]
lista=(7,5,8,7,9,3)
Est= Estructura_estatica(lista)
Est.presentarLista()
Est.usoFor()
Est.buscarLista(3)




