

class Ordenar:
    def __init__(self):
         self.lista=lista

    def recorrerElemento(self):
        for ele in self.lista:
         print(ele)    

    # def recorrerPosicion(self):
    #     for pos,ele in enumerate(self.lista):
    #      print(pos,ele)         
    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
         print(pos,ele)         

    def recorrerRange(self):
        for pos in range(len(self.lista)):
         print(pos,self.lista[pos])       

    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
         if ele == buscado:
             enc=True
             break
        if enc == True:return pos
        else: return-1    
        return pos    

    def ordenarAsc(self):
        for pos in range(0,len(self.lista)):
            for pos in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
         
         


lista = [2,3,1,5,8,10]  
ord1 = Ordenar(lista)    
# ord1.recorrerElemento()
# ord1.recorrerPosicion()
# ord1.recorrerRange()
# print(ord1.buscar(5))
# buscado=9
# resp = ord1.buscar()
# if resp !=-1:
#     print("El numero={} se encuentra en la posicion={}".format(buscado,resp,ord1.lista))
# else:
#     print("El numero={} se encuentra en la posicion={}".format(buscado,resp,ord1.lista))    
print(ord1.lista)
ord1.ordenar()
print(ord1.lista)