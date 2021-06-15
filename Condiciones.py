class Condicion :
   
    def __init__(self,num1=3,num2=8):
        self.numero1=num1
        self.numero2=num2
        numero=self.numero1+self.numero2
        self.numero3=numero

    def usoIf(self):
        #if...elif...else...: permiten condicionar la ejecucion de uno o varios bloques 
        # de sentencias al cumplimiento de una o varias condiciones.
        if self.numero1 == self.numero2:
            print("numero1={}=numero2={}: son iguales".format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1 y numero3 son iguales")   
        else:
            print("numeros diferentes") 
        print("fin if")        

        #print(self.numero3)    

#print('Instancia de la clase')
cond1= Condicion(11,11)
#cond2= Condicion()
#print(cond2.numero3)

cond1.usoIf()
#cond2.usoIf()

#cond1.usoIf()
print('gracias por la visita')