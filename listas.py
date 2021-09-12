  
class Lista:
    def __init__(self,tamanio=3):
        self.lista = []
        self.longitud = 0
        self.size = tamanio
    
    def append(self, dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud +=1
        else:
            print("Lista esta llena")

    def obtener(self, pos): 
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]
    
    def obtenerEliminado(self, pos):
       
        if pos < 0 or pos >= self.longitud:
                return None
        else:
            eliminado = self.lista[pos]
            self.lista = self.lista[:pos]+ self.lista[pos+1:]
            return [self.lista,eliminado]

## Busca un dato en la lista y retorna la posicion de ese valor en la lista
    def buscar(self,dato):   
        pass  
    
## Busca un dato con el metodo buscar y si no lo encuentra lo inserta en la lista
    def insertar(self,dato):  
        pass

## Busca el dato con el metodo buscar y si lo encuentra lo elimina de la lista
    def eliminar(self,dato):  
        pass

    def mostrar(self):
        print("{:2} {:9} {}".format("","Lista","Posición"))
        for pos,ele in enumerate(self.lista):
            print("[{:10}] {:3}".format(ele,pos))


lista1= Lista()
lista1.append("Emanuel")
lista1.append(24)
lista1.append(True)
lista1.mostrar()
posicion = int(input("Ingrese posicion para obtener el elemento: "))
resp = lista1.obtenerEliminado(posicion)
if resp == None:
    print("Posicion no valida, verifique la lista...!!!")
else:
    print("El elemento de la posicion: {} es: {} ".format(posicion,resp))