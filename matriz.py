class Matriz:
    def __init__(self,matriz):
        self.matriz = matriz
        
    def ingresar(self,dato):
        pass
    
    def presentar(self):
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print(self.matriz[fila][col],end=" ")
            print()    
    
    
#columnas   0 1 2   0 1 2    0  1  2
numeros = [[1,2,4,2,1],[1,4,2,6,9],[22,5,95,1,0]]
#filas        0       1         2

#col = numeros[0]
#print(numeros[0],numeros[0][1])
#print(col,col[1])
mat = Matriz(numeros)
mat.presentar()