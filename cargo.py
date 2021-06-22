class Cargo:
    def __init__(self): 
        self.__codigo=99
        self.descripcion= "Sin cargo"

# cargo1= Cargo()        
# print(cargo1.codigo,cargo1.descripcion)
# cargo2= Cargo()
# cargo2.codigo=1
# cargo2.descripcion="Docente"
# print(cargo2.codigo,cargo2.descripcion)
# cargo3= Cargo() 
# cargo3.descripcion="conserje"       
# print(cargo3.codigo,cargo3.descripcion)
cargo1= Cargo()        
print("cargo1",cargo1.descripcion)
cargo2= Cargo()

cargo2.descripcion="Docente"
print("cargo2",cargo2.descripcion)
cargo3= Cargo() 
cargo3.descripcion="conserje"       
print("cargo3",cargo3.descripcion)