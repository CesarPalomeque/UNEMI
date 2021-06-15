class Ciclo:

    def __init__(self,numero=5):
        self.numero= numero
        self.numero2=0

    def usoWhile(self): 
        # ciclo repetitivo que se ejecuta mientras la condicion se cumpla(verdadero),
        # #  es decir sale por falso 
        car = input("ingrese vocal") 
        car = car.lower()
        while car not in('a','e','i','0','u'):
            car1= input("Ingrese vocal").lower()
        print("Felicitacion su vocal es: {}".format(car))    


ciclo1= Ciclo()
ciclo1.usoWhile() 
print("Fin de uso ciclo")       

